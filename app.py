# app.py
# Streamlit portfolio for Harivadan Kilambi
# With glowing animated background, resume download, and elegant layout

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Harivadan Kilambi — AI Engineer & Data Scientist", page_icon="💼", layout="wide")

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
    :root {
      --bg1: #0b1020;
      --bg2: #111827;
      --accent1: #7c3aed;
      --accent2: #ec4899;
      --accent3: #facc15;
    }

    html, body, [class*="css"] {
      margin: 0;
      padding: 0;
      background: linear-gradient(-45deg, var(--bg1), var(--bg2), #1e1b4b, #0f172a);
      background-size: 400% 400%;
      animation: gradientBG 15s ease infinite;
      color: #e6eef8;
      font-family: 'Poppins', sans-serif;
    }

    @keyframes gradientBG {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    h1, h2, h3 {
      background: linear-gradient(90deg, var(--accent1), var(--accent2), var(--accent3));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: gradientShift 5s ease infinite;
      background-size: 300% 300%;
    }

    @keyframes gradientShift {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    .card {
      background: rgba(255, 255, 255, 0.05);
      padding: 18px;
      border-radius: 16px;
      transition: all 0.4s ease;
      border: none;
    }

    .card:hover {
      transform: translateY(-6px) scale(1.02);
      box-shadow: 0 8px 25px rgba(124, 58, 237, 0.3);
      border: 1px solid rgba(124, 58, 237, 0.4);
    }

    .tech-badge {
      display:inline-block;
      padding:8px 14px;
      margin:6px;
      border-radius:999px;
      background:#0b1220;
      color:#cbd5e1;
      font-size:14px;
      transition: all 0.3s ease-in-out;
    }

    .tech-badge:hover {
      background: linear-gradient(90deg, var(--accent1), var(--accent2), var(--accent3));
      color:white;
      transform: scale(1.1);
      box-shadow: 0 0 20px rgba(236,72,153,0.5);
    }

    a { color: #9ae6b4; text-decoration: none; transition: color 0.3s ease; }
    a:hover { color: #f472b6; }

    /* Hide Streamlit's search bar */
    [data-testid="stToolbar"] { visibility: hidden !important; }

    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Header ----------
col1, col2 = st.columns([1, 3], gap="large")
with col1:
    try:
        profile_pic = Image.open("assets/profile.png (2).jpeg")
        st.image(profile_pic, width=160)
    except:
        st.warning("Profile image not found in assets folder!")

with col2:
    st.markdown("<h1>Harivadan Kilambi</h1>", unsafe_allow_html=True)
    st.markdown(
        "AI Engineer | Data Scientist | AI/ML Enthusiast | Builder of Agentic RAG Systems & Streamlit Apps"
    )
    st.markdown("📍 Hyderabad, India | 📧 kilambihari@gmail.com")
    st.download_button("📄 Download Resume", open("assets/HariKilambi_Resume.pdf", "rb"), file_name="HariKilambi_Resume.pdf")

st.write("---")

# ---------- About ----------
st.header("👨‍💼 About Me")
st.write(
    """
I’m a **Computer Science (Data Science)** graduate (2021–2025) passionate about **AI/ML, Generative AI, and multi-agent systems**.  
I specialize in **LangChain, Gemini, Streamlit, and RAG (Retrieval-Augmented Generation)** architectures. Expanding my knowledge in 
AI by completing speciliazed courses and regularly following the latest trends , with strong skills in Data Analysis, Machine Learni-
ng, and Visualization. Seeking real-world experience to apply and grow technical and analytical skills in a professional setting.

Beyond coding, I’m deeply interested in Indian culture, vegetarian lifestyle, and technology for impact.
"""
)

st.write("---")

# ---------- Skills ----------
st.header("🧠 Technical Skills")

skills = {
    "Languages": ["Python", "C", "R Programming"],
    "Libraries & Frameworks": [
        "TensorFlow", "PyTorch", "Keras", "Scikit-learn",
        "Pandas", "NumPy", "LangChain", "Google Gemini API",
        "Streamlit", "Hugging Face", "Django", "NLTK"
    ],
    "Database & Tools": ["MySQL", "SQL", "FAISS", "Jupyter", "VS Code", "Git", "GitHub"],
    "Visualization": ["PowerBI", "Tableau", "Matplotlib", "Seaborn"],
    "Big Data Technologies": ["Hadoop", "Hive", "Apache Spark", "Kafka"],
    "Concepts": ["Machine Learning", "Deep Learning", "RAG Systems", "NLP", "MCP Architecture"]
}

for category, items in skills.items():
    st.subheader(category)
    skill_html = "".join([f"<span class='tech-badge'>{i}</span>" for i in items])
    st.markdown(skill_html, unsafe_allow_html=True)

st.write("---")

# ---------- Projects ----------
st.header("🚀 Featured Projects")

projects = [
    {
        "title": "Agentic RAG Chatbot (Gemini + MCP)",
        "desc": """A multi-agent RAG chatbot using Gemini, FAISS, and MCP-style message passing. Deployed directly via GitHub.
                 Designed Ingestion agent, Retrieval agent, and LLMResponse agent for modular, scalable architecture, enabl-
                 ing efficient message passing between agents. Integrated Streamlit UI for real-time document upload, search,
                 and conversational Q&A with context aware responses.""",
        "tech": ["Python", "Gemini API", "MCP", "FAISS", "Streamlit", "RAG", "NLP", "Pandas"]
    },
    {
        "title": "AI Marketing Idea Generator",
        "desc": """Streamlit app that generates ad copies, slogans, and campaign ideas using Gemini & LangChain. Gets results in
                 formats suitable for Social media, Email Marketing, web banners and more. An API key is loaded from Streamlit 
                 secrets. A custom wrapper around Gemini is built by extending langchain.llms.base.LLM. LangChain’s LLMChain is 
                 used to call Gemini and return results.""",
        "tech": ["LangChain", "Gemini API", "Streamlit", "Python"]
    },
    {
        "title": "Employee Career Path Prediction using AI",
        "desc": """Developed a proof-of-concept AI solution to predict employee performance using a Random Forest model and visua-
                 lize career paths using a Markov chain. Engineered a full-stack, proof-of-concept AI solution for HR analytics, 
                 demonstrating the potential for predicting employee performance, recommending training, and visualizing career 
                 paths. Engineered a user-friendly, interactive dashboard with Streamlit to present key insights and model outpu-
                 ts.""",
        "tech": ["Gemini", "Scikit-learn", "Streamlit", "Pandas", "Python"]
    }
]

for p in projects:
    st.markdown(f"""
        <div class='card'>
            <h3>{p['title']}</h3>
            <p>{p['desc']}</p>
            {''.join(f"<span class='tech-badge'>{t}</span>" for t in p['tech'])}
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------- Experience ----------
st.header("💼 Experience")
st.write("**AI Engineer Intern — Workcohol (Remote)**  — Mar 2025 to Jun 2025")
st.write(
    """
- Built AI-driven predictive analytics and NLP solutions  
- Developed Streamlit dashboards integrating Gemini + LangChain  
- Automated RAG pipelines for real-time knowledge retrieval
"""
)

st.write("---")

# ---------- Contact ----------
st.header("📫 Get in Touch")
st.write("If you’d like to collaborate or hire me, reach out via email or connect below:")

# LinkedIn and GitHub icons
st.markdown("""
<div style="display:flex; gap:20px; align-items:center; justify-content:center; padding:20px;">
    <a href="https://linkedin.com/in/harikilambi" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
    </a>
    <a href="https://github.com/kilambihari" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="40">
    </a>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Contact form (without search)
st.header("💬 Contact Form")

st.write("Send me a message directly 👇")

col1, col2 = st.columns([1, 2])
with col1:
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
with col2:
    message = st.text_area("Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("✅ Message received! (This demo doesn’t send emails — please reach out via email directly.)")
    else:
        st.error("⚠️ Please fill all fields before sending.")

st.write("---")
st.caption("© 2025 Harivadan Kilambi | Built with ❤️ using Streamlit")

