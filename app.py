import streamlit as st
import base64

# --- Page Configuration ---
st.set_page_config(page_title="RealHaven – AI-Powered Estate Search Platform", layout="centered")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://github.com/zeynnepps/realhaven-capstone/blob/master/logo-modified.png" width="150">
            <h1 style="margin-top: 10px;">RealHaven</h1>
        </div>
        """,
        unsafe_allow_html=True
    )


# --- Project Description ---
st.markdown("""
📍 Built for San Jose – Tailored specifically to the local market

🤖 AI-Powered Chatbot – Guides users through property search naturally

🎯 Smart Filtering – Matches listings to user needs & preferences

📊 Visual Insights – Graphs help compare prices and features

🏷️ Detailed Property Views – See kitchen, living room, and more

🚀 Simplified Experience – Makes home search faster and more informed      
""")

# --- Methodology ---
st.markdown("## 🧪 Methodology")
st.markdown("""
We combined **AI development**, **web app design**, and **ML techniques** to deliver RealHaven:
- Collected and cleaned a dataset of **1000+ San Jose listings**
- Built a custom **NLP-based chatbot** using **spaCy** and **NER**
- Designed a **dynamic frontend** using React.js
- Enabled **image-enhanced search** and fallback query handling
- Integrated user roles: **Admin** (manages listings) & **Buyer/Renter** (searches, saves, rents)
""")

# --- AI Chatbot Functionality ---
st.markdown("## 💬 RealHaven AI Assistant")
st.markdown("""
Our assistant supports:
- Natural language queries like *"3-bed homes under $2M in San Jose"*
- Visual property results with room images
- **NER-based filtering** and multilingual greetings
- Future upgrades: smarter fallbacks, complex query understanding
""")

# --- Summary / Conclusion ---
st.markdown("## ✅ Summary / Conclusion")
st.markdown("""
We integrated **Multimodal Intelligence** into RealHaven by combining:

- 🧠 **Text-based search** using natural language queries  
- 🖼️ **Room-level images** (e.g., bedroom, kitchen, bathroom) to enhance property exploration  

As a result, users can:

- 🔎 Search naturally (e.g., *“2BHK with modern kitchen in San Jose”*)  
- 🏠 View detailed visuals of each room directly within the chatbot  
- 💡 Receive **context-rich, image-enhanced property recommendations**

This approach moves beyond traditional search, offering a **more intelligent and intuitive real estate experience**.
""")

# --- Acknowledgment ---
st.markdown("## 🙏 Acknowledgment")
st.markdown("""
We thank **Professor Ahmed Banafa** for his guidance and encouragement throughout this project.  
His insights played a key role in shaping and developing RealHaven.
""")

# --- Team Members ---
st.markdown("## 👥 Meet the Team")
team_members = [
    {"name": "Zeynep Salihoglu", "linkedin": "http://linkedin.com/in/zeynep-salihoglu"},
    {"name": "Vyshnavi Akkapalli", "linkedin": "http://linkedin.com/in/vyshnavi-akkapalli-484a5b208"},
    {"name": "Raghav Venkata Krishna", "linkedin": "http://www.linkedin.com/in/raghav-katari-786899306"},
    {"name": "Hassan Ahmed", "linkedin": "https://www.linkedin.com/in/hassan-ahmed-siddiqui-aa22a51a0"},
]
for member in team_members:
    st.markdown(f"- [{member['name']}]({member['linkedin']})" if member["linkedin"] else f"- {member['name']}")

def set_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cms.nar.realtor/sites/default/files/downloadable/commercial_primary_img_1300x867-2023-01-30.jpg");
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