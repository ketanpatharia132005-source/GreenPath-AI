import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def load_knowledge_base():
    file_path = "data/green_knowledge.txt"

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def split_into_chunks(text):
    paragraphs = text.split("\n\n")
    chunks = []

    for para in paragraphs:
        clean_para = para.strip()
        if clean_para:
            chunks.append(clean_para)

    return chunks


def calculate_score(question, chunk):
    question_words = question.lower().split()
    chunk_lower = chunk.lower()

    score = 0

    for word in question_words:
        if word in chunk_lower:
            score += 1

    return score


def retrieve_context(question, chunks, top_k=3):
    scored_chunks = []

    for chunk in chunks:
        score = calculate_score(question, chunk)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    best_chunks = [chunk for score, chunk in scored_chunks[:top_k] if score > 0]

    return "\n\n".join(best_chunks)


def rag_answer(question):
    knowledge_text = load_knowledge_base()

    if knowledge_text is None:
        return "Knowledge file not found. Please add green_knowledge.txt inside the data folder."

    if knowledge_text.strip() == "":
        return "Knowledge file is empty. Please add content inside green_knowledge.txt."

    chunks = split_into_chunks(knowledge_text)

    if len(chunks) == 0:
        return "No readable content found in the knowledge file."

    context = retrieve_context(question, chunks)

    if context.strip() == "":
        return "Sorry, I could not find relevant information in the knowledge base."

    prompt = f"""
You are GreenPath AI, a sustainability and SDG assistant.

Use the given knowledge base context to answer the user's question.

Rules:
- Answer only what the user asked.
- Do not explain the RAG process.
- Do not write unnecessary project details.
- Do not mention "knowledge base" in the final answer.
- Keep the answer simple, clear, and student-friendly.
- If the user asks "What is SDG 13?", explain SDG 13 and related climate action information only.

Context:
{context}

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
            max_tokens=500
        )

        answer = response.choices[0].message.content
        return answer

    except Exception as e:
        return f"Error while generating answer: {e}"