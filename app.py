import streamlit as st

st.set_page_config(page_title="Path to ML Engineer", page_icon="🧑‍💻", layout="wide")

# Title
st.title("🧑‍💻 Path to ML Engineer")
st.write("A roadmap of essential skills and resources to grow from beginner → expert in ML Engineering.")

# Sidebar
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("[Introduction](#introduction)")
st.sidebar.markdown("[Core Skills](#core-skills)")
st.sidebar.markdown("[Tools & Frameworks](#tools--frameworks)")
st.sidebar.markdown("[Learning Resources](#learning-resources)")
st.sidebar.markdown("[Career Growth](#career-growth)")

# Sections
st.header("📖 Introduction")
st.write("""
Machine Learning Engineering is about taking models from research → production.
This roadmap highlights the **core skills, tools, and resources** you need to master.
""")

st.header("🛠️ Core Skills")
skills = {
    "Programming": ["Python (pandas, numpy, OOP)", "SQL", "Data Structures & Algorithms"],
    "ML Basics": ["Supervised vs Unsupervised", "Model evaluation (precision/recall, ROC)", "Feature engineering"],
    "Math & Stats": ["Probability", "Linear Algebra", "Calculus", "Optimization"],
    "Data Engineering": ["ETL pipelines", "Data Warehousing", "Big Data basics (Spark/Hadoop)"]
}
for category, items in skills.items():
    st.subheader(category)
    st.write("• " + "\n• ".join(items))

st.header("⚙️ Tools & Frameworks")
st.markdown("""
- **ML Libraries** → scikit-learn, TensorFlow, PyTorch  
- **Model Serving** → FastAPI, Flask, Streamlit  
- **MLOps** → MLflow, Kubeflow, Airflow, Docker, Kubernetes  
- **Cloud Platforms** → AWS Sagemaker, GCP Vertex AI, Azure ML  
""")

st.header("📚 Learning Resources")
st.markdown("""
**Free Resources:**
- [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)  
- [CS229 Stanford ML](https://cs229.stanford.edu/)  
- [FastAPI Docs](https://fastapi.tiangolo.com/)  
- [Streamlit Docs](https://docs.streamlit.io/)  

**Paid Resources:**
- Coursera ML Engineering Specialization  
- Udemy MLOps courses  
""")

st.header("🚀 Career Growth")
st.write("""
- Start with **data cleaning & pipelines** → build SQL + pandas strength.  
- Move to **model training & evaluation** → scikit-learn, TensorFlow/PyTorch.  
- Learn **deployment** → FastAPI, Docker, CI/CD.  
- Finally, **MLOps & scaling** → MLflow, Airflow, Kubernetes, Cloud ML.  

💡 Pro Tip: Document everything, write clean code, and collaborate using Git/GitHub.
""")

st.success("✨ Keep building projects, sharing work, and you’ll become an ML Engineer in demand!")
