import streamlit as st
from groq import Groq
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Viral Post Creation",
    page_icon="💡",
    layout="centered"
)

# ---------------- API SETUP ----------------
# Set your API key safely (recommended)
# os.environ["GROQ_API_KEY"] = "your_api_key_here"

# api_key = os.getenv("GROQ_API_KEY")
api_key="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"

try:
    client = Groq(api_key=api_key)
except Exception:
    st.error("API Key Error... Please check your key")
    st.stop()

# ---------------- UI ----------------
st.title("AI Viral Post Creation ")
st.markdown("---")
st.write("Enter your topic and get a viral LinkedIn / Instagram post")

topic = st.text_area(
    "What is your post about?",
    placeholder="Ex: My first day of learning AI with Python"
)

language = st.selectbox(
    "Select Language:",
    ["Tamil", "English", "Tanglish"]
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    generate_btn = st.button(
        "Generate Post",
        type="primary",
        use_container_width=True
    )

# ---------------- LOGIC ----------------
if generate_btn:
    if not topic.strip():
        st.warning("Please enter a topic!")
    else:
        try:
            with st.spinner("AI is thinking... 💡"):
                prompt = f"""
Act as a professional social media influencer.

Write an engaging, viral LinkedIn/Instagram post about:
"{topic}"

STRICT REQUIREMENT:
Write the post in **{language}**

Rules:
1. Start with a catchy hook/headline
2. Use bullet points
3. Include relevant emojis
4. End with a question to the audience
5. Add 5 trending hashtags
"""

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                ai_response = response.choices[0].message.content

            st.balloons()
            st.success("Your viral post is ready! 🎉")
            st.markdown(ai_response)
            st.info("Tip: Copy this and post it on LinkedIn / Instagram")

        except Exception as e:
            st.error(f"Error: {e}")
