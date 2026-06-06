def generate_project_idea(domain, level, duration, sdg):
    ideas = {
        "Education": {
            "title": "EduGreen AI Mentor",
            "problem": "Many students do not know how to connect their technical skills with sustainability and SDGs.",
            "solution": "An AI-based mentor that suggests sustainability learning paths and project ideas for students.",
            "sdg": "SDG 4: Quality Education",
            "features": [
                "Personalized learning roadmap",
                "SDG-based project suggestions",
                "Beginner-friendly explanations",
                "Impact report generator"
            ]
        },
        "Climate Action": {
            "title": "ClimateWise RAG Assistant",
            "problem": "People find it difficult to understand climate change information from long documents.",
            "solution": "A RAG-based chatbot that answers climate-related questions using trusted sustainability documents.",
            "sdg": "SDG 13: Climate Action",
            "features": [
                "Climate change Q&A chatbot",
                "RAG-based document search",
                "Simple climate explanations",
                "Action tips for students"
            ]
        },
        "Employability": {
            "title": "Green Career Path AI",
            "problem": "Students are unaware of green jobs and the skills required for sustainability careers.",
            "solution": "An AI tool that recommends green career paths, skills, and projects based on student interest.",
            "sdg": "SDG 8: Decent Work and Economic Growth",
            "features": [
                "Green job role suggestions",
                "Skill gap analysis",
                "Career roadmap generation",
                "Project-based learning guide"
            ]
        },
        "Waste Management": {
            "title": "EcoSort AI Guide",
            "problem": "Many people do not know how to separate and manage waste properly.",
            "solution": "A smart assistant that educates users about waste categories and responsible disposal.",
            "sdg": "SDG 12: Responsible Consumption and Production",
            "features": [
                "Waste category guidance",
                "Recycling awareness",
                "E-waste disposal tips",
                "Community awareness content"
            ]
        },
        "Energy": {
            "title": "Smart Energy Awareness AI",
            "problem": "Students and households often waste electricity due to lack of awareness.",
            "solution": "An AI-powered guide that suggests simple ways to save energy and reduce carbon footprint.",
            "sdg": "SDG 7: Affordable and Clean Energy",
            "features": [
                "Energy saving tips",
                "Daily habit suggestions",
                "Electricity usage awareness",
                "Sustainability score"
            ]
        }
    }

    selected = ideas.get(sdg)

    project_text = f"""
## {selected['title']}

### Problem Statement
{selected['problem']}

### Proposed Solution
{selected['solution']}

### SDG Alignment
{selected['sdg']}

### Recommended Tech Stack
- Domain: {domain}
- Level: {level}
- Duration: {duration}
- Frontend: Streamlit
- Backend: Python
- AI: RAG-based chatbot
- Database: FAISS vector database

### Main Features
"""

    for feature in selected["features"]:
        project_text += f"- {feature}\n"

    project_text += f"""

### Why this project is useful
This project helps students and communities understand sustainability in a simple way. It connects technology with real-world social and environmental impact.

### Final Outcome
A working AI-based sustainability project that can be shown in your 1M1B internship presentation.
"""

    return project_text