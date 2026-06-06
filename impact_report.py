def generate_impact_report(project_name, problem, target_users, sdgs):
    report = f"""
## Impact Report: {project_name}

### Problem Statement
{problem}

### Target Users
{target_users}

### SDGs Covered
{sdgs}

---

## Expected Impact

This project creates social and environmental impact by helping users understand sustainability problems and take informed action.

### Educational Impact
- Helps students understand SDGs in simple language.
- Encourages project-based learning.
- Supports awareness about sustainability and green skills.

### Social Impact
- Helps communities identify real-world problems.
- Promotes responsible behavior.
- Encourages youth participation in sustainability.

### Environmental Impact
- Supports awareness about climate action, waste management, energy saving, and responsible consumption.
- Encourages eco-friendly decisions.

---

## Innovation

This project uses AI and RAG to provide more useful and context-based guidance. Instead of giving random answers, the system retrieves information from a knowledge base and then provides relevant responses.

---

## Future Scope

- Add PDF upload support.
- Add Gemini/OpenAI-powered answers.
- Add downloadable PDF reports.
- Add user login and saved project history.
- Add multilingual support for rural students.

---

## Final Summary

{project_name} supports sustainability by connecting students, technology, and SDG-based problem solving. It can help learners choose better project ideas, understand impact, and prepare meaningful solutions for real-world challenges.
"""

    return report