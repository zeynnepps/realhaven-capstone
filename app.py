import streamlit as st

#Logo
st.image("logo.jpeg", width=150)  # Adjust width as needed

# Page config
st.set_page_config(page_title="RealHaven – Al-Powered Estate Search Platform", layout="centered")

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
            background-image: url("https://www.google.com/imgres?q=webpage%20background%20sky&imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F912110%2Fpexels-photo-912110.jpeg%3Fcs%3Dsrgb%26dl%3Dpexels-elia-clerici-282848-912110.jpg%26fm%3Djpg&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fsky%2520background%2F&docid=HJ2rcpasoJqA2M&tbnid=42upTsvmPqO-YM&vet=12ahUKEwie8frA0PGMAxWOweYEHQeMELMQM3oECBoQAA..i&w=6000&h=4000&hcb=2&ved=2ahUKEwie8frA0PGMAxWOweYEHQeMELMQM3oECBoQAA");
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

