import json
import streamlit as st
from fuzzywuzzy import process

# --- Load large FAQ dataset ---
with open("faqs_large.json", "r") as f:
    faqs = json.load(f)

# Prepare list of all questions for fuzzy matching
faq_questions = [item["question"] for item in faqs]

# --- Fuzzy matching function ---
def get_best_faq_answer(user_input, limit=1, threshold=60):
    """
    Returns the best matching FAQ answer for the user input.
    limit: number of top matches to consider
    threshold: minimum match score (0-100) to consider a match
    """
    # Use fuzzywuzzy's process.extract to get top matches
    matches = process.extract(user_input, faq_questions, limit=limit)
    
    if matches:
        best_match, score = matches[0]
        if score >= threshold:
            # Find the answer corresponding to the matched question
            for item in faqs:
                if item["question"] == best_match:
                    return item["answer"]
    
    # Fallback if no good match
    return "Sorry, I couldn't find relevant information in the FAQs. Please consult a doctor for medical advice."

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
        answer = get_best_faq_answer(user_input)
        st.session_state.history.append((user_input, answer))
    else:
        st.warning("Please enter a question.")

# Display chat history
for q, a in st.session_state.history:
    st.markdown(f"<p style='color:blue'><b>You:</b> {q}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:green'><b>Bot:</b> {a}</p>", unsafe_allow_html=True)
    st.markdown("---")

# Clear chat
if st.button("Clear Chat"):
    st.session_state.history = []
