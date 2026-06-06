import os


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


def rag_answer(question):
    knowledge_text = load_knowledge_base()

    if knowledge_text is None:
        return "Knowledge file not found. Please add green_knowledge.txt inside the data folder."

    if knowledge_text.strip() == "":
        return "Knowledge file is empty. Please add content inside green_knowledge.txt."

    chunks = split_into_chunks(knowledge_text)

    if len(chunks) == 0:
        return "No readable content found in the knowledge file."

    scored_chunks = []

    for chunk in chunks:
        score = calculate_score(question, chunk)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    best_chunks = [chunk for score, chunk in scored_chunks[:2] if score > 0]

    if not best_chunks:
        return """
## Answer from GreenPath AI

Sorry, I could not find a strong match in the knowledge base.

Try asking questions like:
- What is SDG 13?
- What is RAG?
- What are green skills?
- Suggest a 15-day sustainability project.
"""

    context = "\n\n".join(best_chunks)

    answer = f"""
## Answer from GreenPath AI Knowledge Base

{context}

---

### Simple Explanation

This answer was generated using a basic RAG process:

1. Your question was received.
2. The system searched the knowledge base.
3. The most relevant information was retrieved.
4. The answer was shown based on that retrieved content.
"""

    return answer