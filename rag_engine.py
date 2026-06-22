import os
from dotenv import load_dotenv
from groq import Groq
import base64

load_dotenv()


def get_groq_api_key():
    api_key = os.getenv("GROQ_API_KEY")

    if api_key:
        return api_key

    try:
        import streamlit as st
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return None


api_key = get_groq_api_key()

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Add it in .env locally or Streamlit Secrets online.")

client = Groq(api_key=api_key)


def load_knowledge_base():
    file_path = "data/green_knowledge.txt"

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def split_into_chunks(text, chunk_size=900, overlap=150):
    """
    This function splits long text into smaller chunks.
    It works for both:
    1. green_knowledge.txt
    2. uploaded documents
    """

    if not text:
        return []

    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    text = " ".join(text.split())

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start = end - overlap

        if start < 0:
            start = 0

        if start >= len(text):
            break

    return chunks


def calculate_score(question, chunk):
    question_words = question.lower().split()
    chunk_lower = chunk.lower()

    score = 0

    for word in question_words:
        clean_word = word.strip(".,?!:;()[]{}'\"")

        if len(clean_word) > 2 and clean_word in chunk_lower:
            score += 1

    return score


def retrieve_context(question, chunks, top_k=4):
    scored_chunks = []

    for chunk in chunks:
        score = calculate_score(question, chunk)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    best_chunks = [chunk for score, chunk in scored_chunks[:top_k] if score > 0]

    return "\n\n".join(best_chunks)


def generate_answer_from_context(question, context, image_note=""):
    prompt = f"""
You are GreenPath AI, a sustainability and SDG assistant.

Use the given context to answer the user's question.

Rules:
- Answer only what the user asked.
- Do not explain the RAG process.
- Do not write unnecessary project details.
- Do not mention "knowledge base" in the final answer.
- Keep the answer simple, clear, and student-friendly.
- Focus on sustainability, SDGs, climate awareness, green skills, and practical suggestions.
- If uploaded document context is available, use it to answer the user's question.
- If image input is mentioned, give an awareness-based environmental explanation.
- If the exact image content is not available, say that the answer is based on the user's question and environmental context.

Context:
{context}

Image Instruction:
{image_note}

User Question:
{question}

Answer:
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful sustainability and SDG assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=600
        )

        answer = response.choices[0].message.content
        return answer

    except Exception as e:
        return f"Error while generating answer: {e}"


def rag_answer(question, uploaded_context="", image_note=""):
    """
    Main RAG answer function.

    It uses:
    1. Permanent knowledge file: data/green_knowledge.txt
    2. Temporary uploaded document context from app.py
    3. Image note if user uploads an image
    """

    knowledge_text = load_knowledge_base()

    all_chunks = []

    # Permanent knowledge file chunks
    if knowledge_text and knowledge_text.strip():
        knowledge_chunks = split_into_chunks(knowledge_text)
        all_chunks.extend(knowledge_chunks)

    # Uploaded document chunks
    if uploaded_context and uploaded_context.strip():
        uploaded_chunks = split_into_chunks(uploaded_context)
        all_chunks.extend(uploaded_chunks)

    # If no knowledge file and no uploaded document
    if len(all_chunks) == 0:
        if image_note.strip():
            context = "The user uploaded an environmental image. Give a sustainability and SDG-based explanation."
            return generate_answer_from_context(question, context, image_note)

        return "No readable content found. Please add green_knowledge.txt inside the data folder or upload a document."

    context = retrieve_context(question, all_chunks)

    # If no matching chunk found, still allow image-based answer
    if context.strip() == "":
        if image_note.strip():
            context = "The user uploaded an environmental image. Give a sustainability and SDG-based explanation."
            return generate_answer_from_context(question, context, image_note)

        return "Sorry, I could not find relevant information. Please ask a more specific question or upload a related document."

    return generate_answer_from_context(question, context, image_note)
def analyze_image_with_groq(uploaded_image, user_question):
    image_bytes = uploaded_image.getvalue()
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    file_type = uploaded_image.type

    if file_type not in ["image/jpeg", "image/png", "image/jpg"]:
        return "Please upload a valid JPG, JPEG, or PNG image."

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are GreenPath-AI, an environmental awareness assistant. "
                    "Analyze the uploaded image carefully. Explain what is visible in the image, "
                    "identify environmental problems if present, and connect it with sustainability "
                    "and SDG 13 Climate Action. "
                    "Do not say that the exact image content is not available if an image is provided."
                ),
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_question,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{file_type};base64,{base64_image}"
                        },
                    },
                ],
            },
        ],
        temperature=0.3,
        max_completion_tokens=700,
    )

    return response.choices[0].message.content