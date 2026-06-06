# 🌱 GreenPath AI

GreenPath AI is a RAG-based sustainability project mentor that helps students discover SDG-aligned project ideas, understand sustainability topics, generate skill roadmaps, match real-world problems with SDGs, and create impact reports.

## 🚀 Project Overview

Many students want to build sustainability-based projects but do not know:

- Which SDG to choose
- What problem to solve
- What skills are required
- How to create project impact
- How to connect technology with sustainability

GreenPath AI solves this problem by acting as an AI-powered sustainability mentor.

## ✨ Features

### 1. Ask GreenPath AI
A basic RAG chatbot that answers questions using a sustainability knowledge base.

Example questions:

- What is SDG 13?
- What is RAG?
- What are green skills?
- Suggest a 15-day sustainability project.

### 2. Project Idea Generator
Generates project ideas based on:

- Domain
- Skill level
- Duration
- SDG area

### 3. SDG Matcher
Matches a real-world problem with relevant Sustainable Development Goals.

### 4. Skill Roadmap Generator
Creates a beginner-friendly roadmap based on the user's current skill and goal.

### 5. Impact Report Generator
Generates a short impact report including:

- Problem statement
- Target users
- SDGs covered
- Expected impact
- Future scope

## 🧠 What is RAG?

RAG stands for Retrieval-Augmented Generation.

In this project, the system first searches the sustainability knowledge base and retrieves relevant information before showing the answer. This makes the answer more focused and useful than a normal static chatbot.

## 🛠️ Tech Stack

- Python
- Streamlit
- Basic RAG logic
- Text-based knowledge base
- Modular Python files

## 📁 Project Structure

```text
greenpath-ai/
│
├── app.py
├── rag_engine.py
├── project_generator.py
├── sdg_matcher.py
├── roadmap_generator.py
├── impact_report.py
├── README.md
│
├── data/
│   └── green_knowledge.txt
│
└── vectorstore/