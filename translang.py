# ======================================
# TransLingua – AI Powered Translator
# Using Latest Google GenAI SDK
# ======================================

from dotenv import load_dotenv
import os
import streamlit as st
from google.genai import Client

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ API Key not found. Check your .env file.")
    st.stop()

# Initialize Gemini client
client = Client(api_key=API_KEY)

# Streamlit UI
st.set_page_config(page_title="AI-Powered Language Translator", page_icon="🌐")
st.title("🌐 AI-Powered Language Translator")
st.write("Translate text between multiple languages using Google Gemini.")

# Translation function
def translate_text(text, source_language, target_language):
    prompt = f"""
    Translate the following text from {source_language} to {target_language}.
    Provide only the translated text.

    Text:
    {text}
    """
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )
    return response.text.strip()

# User inputs
text = st.text_area("✍️ Enter text to translate")

source_language = st.selectbox(
    "🌍 Select source language",
    ["English", "Spanish", "French", "German", "Chinese"]
)

target_language = st.selectbox(
    "🌐 Select target language",
    ["English", "Spanish", "French", "German", "Chinese"]
)

# Translate button
if st.button("🔁 Translate"):
    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Translating..."):
            result = translate_text(text, source_language, target_language)

        st.subheader("📘 Translated Text")
        st.success(result)
