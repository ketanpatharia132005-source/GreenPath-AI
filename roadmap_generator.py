def generate_roadmap(skill, goal):
    skill = skill.lower()
    goal = goal.lower()

    roadmap = f"""
## Personalized Skill Roadmap

### Your Current Skill
{skill}

### Your Goal
{goal}

---

## Phase 1: Strengthen Basics

### Learn or revise:
- Python basics
- Functions
- Lists and dictionaries
- File handling
- Basic error handling

### Mini Task
Create a small Python program that reads a text file and prints important words from it.

---

## Phase 2: Learn AI and RAG Basics

### Learn:
- What is AI
- What is an LLM
- What is RAG
- What are embeddings
- What is a vector database

### Mini Task
Write a short note explaining how RAG is different from a normal chatbot.

---

## Phase 3: Learn Sustainability Concepts

### Learn:
- What are SDGs
- SDG 4: Quality Education
- SDG 8: Decent Work and Economic Growth
- SDG 12: Responsible Consumption and Production
- SDG 13: Climate Action

### Mini Task
Choose one SDG and write one real-world problem related to it.

---

## Phase 4: Build GreenPath AI Features

### Build:
- Project Idea Generator
- SDG Matcher
- Skill Roadmap Generator
- RAG Chatbot

### Mini Task
Add one new SDG-based project idea to your project generator.

---

## Phase 5: Final Project Preparation

### Prepare:
- GitHub repository
- README file
- Screenshots
- Presentation PPT
- 1-minute project explanation

### Final Outcome
You will have a working AI + RAG sustainability project that can be shown in your 1M1B internship presentation.
"""

    return roadmap