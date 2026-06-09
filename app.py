import streamlit as st
from project_generator import generate_project_idea
from sdg_matcher import match_sdg
from roadmap_generator import generate_roadmap
from rag_engine import rag_answer
from impact_report import generate_impact_report
st.set_page_config(
    page_title="GreenPath AI",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 GreenPath AI")
st.subheader("RAG-Based Sustainability Project Mentor")

st.write("""
GreenPath AI helps students discover SDG-aligned project ideas, 
skill roadmaps, and sustainability guidance using AI and RAG.
""")

menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Home",
        "Ask GreenPath AI",
        "Project Idea Generator",
        "SDG Matcher",
        "Skill Roadmap Generator",
        "Impact Report Generator"
    ]
)
st.sidebar.markdown("---")
st.sidebar.info("""
🌱 **GreenPath AI**

AI + RAG based sustainability mentor for students.

Built for:
- SDG awareness
- Project guidance
- Skill roadmap
- Impact reporting
""")

if menu == "Home":
    st.header("Welcome to GreenPath AI 🌱")

    st.markdown("""
    ## What is GreenPath AI?

    **GreenPath AI** is a RAG-based sustainability project mentor that helps students
    discover SDG-aligned project ideas, understand sustainability topics, generate skill
    roadmaps, and connect technology with real-world impact.

    ---

    ## Main Features
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.info("🌍 **Ask GreenPath AI**\n\nAsk questions about SDGs, green skills, sustainability, RAG, and project ideas.")
        st.success("💡 **Project Idea Generator**\n\nGenerate sustainability project ideas based on domain, level, duration, and SDG area.")

    with col2:
        st.warning("🎯 **SDG Matcher**\n\nEnter a real-world problem and find which SDG it connects with.")
        st.error("🛣️ **Skill Roadmap Generator**\n\nGet a beginner-friendly roadmap to build AI and sustainability projects.")

    st.markdown("""
    ---

    ## SDGs Covered

    - **SDG 4:** Quality Education  
    - **SDG 7:** Affordable and Clean Energy  
    - **SDG 8:** Decent Work and Economic Growth  
    - **SDG 12:** Responsible Consumption and Production  
    - **SDG 13:** Climate Action  

    ---

    ## Why this project is useful

    Many students want to work on sustainability but do not know which project to build,
    which SDG to choose, or which skills are required. GreenPath AI solves this by acting
    as a personal AI mentor for sustainability-based project building.
    """)

elif menu == "Ask GreenPath AI":
    st.header("Ask GreenPath AI")
    st.write("Ask questions about SDGs, green skills, sustainability, RAG, or project ideas.")

    user_question = st.text_input("Ask any sustainability or SDG-related question:")

    if st.button("Get Answer"):
        if user_question.strip():
             with st.spinner("Generating answer..."):
                answer = rag_answer(user_question)

        st.subheader("Answer")
        st.markdown(answer)        
    else:
            st.warning("Please enter a question.")

elif menu == "Project Idea Generator":
    st.header("Project Idea Generator")

    domain = st.selectbox("Select your domain", ["AI", "Web Development", "Data Science", "IoT"])
    level = st.selectbox("Select your level", ["Beginner", "Intermediate"])
    duration = st.selectbox("Project duration", ["7 Days", "15 Days", "30 Days"])
    sdg = st.selectbox("Select SDG area", ["Education", "Climate Action", "Employability", "Waste Management", "Energy"])

    if st.button("Generate Project Idea"):
        idea = generate_project_idea(domain, level, duration, sdg)
        st.markdown(idea)

elif menu == "SDG Matcher":
    st.header("SDG Matcher")

    problem = st.text_area("Enter a real-world problem:")

    if st.button("Match SDG"):
        if problem:
            result = match_sdg(problem)
            st.markdown(result)
        else:
            st.warning("Please enter a problem.")
elif menu == "Skill Roadmap Generator":
    st.header("Skill Roadmap Generator")

    skill = st.text_input("Enter your current skill:")
    goal = st.text_input("Enter your goal:")

    if st.button("Generate Roadmap"):
        if skill and goal:
            roadmap = generate_roadmap(skill, goal)
            st.markdown(roadmap)
        else:
            st.warning("Please enter both current skill and goal.")

elif menu == "Impact Report Generator":
    st.header("Impact Report Generator")

    project_name = st.text_input("Enter your project name:")
    problem = st.text_area("Enter the problem your project solves:")
    target_users = st.text_input("Enter target users:")
    sdgs = st.text_input("Enter SDGs covered:")

    if st.button("Generate Impact Report"):
        if project_name and problem and target_users and sdgs:
            report = generate_impact_report(project_name, problem, target_users, sdgs)
            st.markdown(report)
        else:
            st.warning("Please fill all fields.")            