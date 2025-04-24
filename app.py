import streamlit as st


# Page config
st.set_page_config(page_title="RealHaven – Al-Powered Estate Search Platform", layout="centered")

st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

#Logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo-modified.png", width=150)

# --- Title ---
st.title("🏡 RealHaven – Your Smart Real Estate Assistant")

# --- Project Description ---
st.markdown("""
📍 Built for San Jose – Tailored specifically to the local market

🤖 AI-Powered Chatbot – Guides users through property search naturally

🎯 Smart Filtering – Matches listings to user needs & preferences

📊 Visual Insights – Graphs help compare prices and features

🏷️ Detailed Property Views – See kitchen, living room, and more

🚀 Simplified Experience – Makes home search faster and more informed      
""")

# --- Meet the Team ---
st.subheader("👥 Meet the Team")

team_members = [
    {"name": "Zeynep Salihoglu", "linkedin": "http://linkedin.com/in/zeynep-salihoglu"},
    {"name": "Vyshnavi Akkapalli", "linkedin": "http://linkedin.com/in/vyshnavi-akkapalli-484a5b208"},
    {"name": "Raghav Venkata Krishna", "linkedin": "http://www.linkedin.com/in/raghav-katari-786899306"},
    {"name": "Hassan Ahmed", "linkedin": ""},
]

for member in team_members:
    st.markdown(f"- [{member['name']}]({member['linkedin']})")

def set_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://img.freepik.com/premium-photo/gradient-aquatic-rough-abstract-background-design_851755-330071.jpg?semt=ais_hybrid&w=740");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()
