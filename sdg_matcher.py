def match_sdg(problem):
    problem = problem.lower()

    if "education" in problem or "student" in problem or "school" in problem or "learning" in problem or "career" in problem:
        return """
## Matched SDGs

### SDG 4: Quality Education
This problem is related to education, learning, awareness, and student development.

### SDG 8: Decent Work and Economic Growth
If the problem is related to career guidance, employability, skills, or jobs, it also connects with SDG 8.

### Suggested Project Direction
Build an AI-based learning or career guidance platform that helps students get proper skill roadmaps and project ideas.
"""

    elif "climate" in problem or "pollution" in problem or "carbon" in problem or "environment" in problem:
        return """
## Matched SDG

### SDG 13: Climate Action
This problem is related to climate change, pollution, environmental awareness, or carbon emissions.

### Suggested Project Direction
Build a RAG-based climate awareness chatbot that explains climate problems and suggests simple actions.
"""

    elif "waste" in problem or "plastic" in problem or "recycle" in problem or "e-waste" in problem:
        return """
## Matched SDGs

### SDG 12: Responsible Consumption and Production
This problem is related to waste management, recycling, and responsible use of resources.

### SDG 13: Climate Action
Reducing waste also helps reduce environmental damage and supports climate action.

### Suggested Project Direction
Build an AI waste-sorting guide or e-waste awareness assistant.
"""

    elif "energy" in problem or "electricity" in problem or "power" in problem or "solar" in problem:
        return """
## Matched SDG

### SDG 7: Affordable and Clean Energy
This problem is related to clean energy, electricity saving, renewable energy, or solar power.

### Suggested Project Direction
Build a smart energy awareness assistant that gives energy-saving suggestions.
"""

    elif "job" in problem or "skill" in problem or "employment" in problem or "internship" in problem:
        return """
## Matched SDG

### SDG 8: Decent Work and Economic Growth
This problem is related to jobs, skills, employment, internships, and career growth.

### Suggested Project Direction
Build a green career path AI tool that recommends sustainability career skills and projects.
"""

    else:
        return """
## General SDG Match

This problem can be connected with sustainability depending on its context.

### Possible SDGs
- SDG 4: Quality Education
- SDG 8: Decent Work and Economic Growth
- SDG 9: Industry, Innovation and Infrastructure
- SDG 12: Responsible Consumption and Production
- SDG 13: Climate Action

### Suggested Project Direction
Use GreenPath AI to analyze the problem further and generate an SDG-aligned project idea.
"""