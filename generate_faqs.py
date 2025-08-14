import json
import streamlit as st
from fuzzywuzzy import process

# --- Load FAQ dataset with categories and tags ---
with open("faqs_large.json", "r") as f:
    faqs = json.load(f)

# --- Prepare data for faster matching ---
faq_questions = [item["question"] for item in faqs]

# --- Fuzzy matching with tags ---
def get_best_faq_answer(user_input, limit=5, threshold=60):
    """
    Returns the best matching FAQ answer with category and highlighted keywords.
    """
    # First, filter by tags in user input
    tag_matches = []
    user_words = set(user_input.lower().split())
    for item in faqs:
        tags = set(item.get("tags", []))
        if tags & user_words:
            tag_matches.append(item)
    search_space = tag_matches if tag_matches else faqs

    # Fuzzy match in the selected search space
    questions = [item["question"] for item in search_space]
    matches = process.extract(user_input, questions, limit=limit)
    
    if matches:
        best_match, score = matches[0]
        if score >= threshold:
            for item in search_space:
                if item["question"] == best_match:
                    # Highlight keywords from tags if available
                    answer = item["answer"]
                    for kw in item.get("tags", []):
                        answer = answer.replace(kw, f"**{kw}**")
                    category = item.get("category", "General")
                    return category, answer
    return "General", "Sorry, I couldn't find relevant information. Please consult a doctor."

# --- Streamlit UI ---
st.set_page_config(page_title="Healthcare Chatbot", page_icon="🤖", layout="centered")
st.title("Healthcare Chatbot 🤖")
st.write("Ask about your symptoms or general health questions:")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", key="user_input")

if st.button("Ask"):
    if user_input.strip():
        category, answer = get_best_faq_answer(user_input)
        st.session_state.history.append((user_input, category, answer))
    else:
        st.warning("Please enter a question.")

# Display chat history
for q, cat, a in st.session_state.history:
    st.markdown(f"""
        <div style='background-color:#d1f7ff;padding:10px;border-radius:10px;margin-bottom:5px;'>
            <b>You:</b> {q}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='background-color:#e2ffe2;padding:10px;border-radius:10px;margin-bottom:10px;'>
            <b>{cat} 🤖</b><br>
            <details>
                <summary>View Answer</summary>
                <p>{a}</p>
            </details>
        </div>
    """, unsafe_allow_html=True)

# Clear chat
if st.button("Clear Chat"):
    st.session_state.history = []
