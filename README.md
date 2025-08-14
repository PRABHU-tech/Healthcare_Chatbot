# 🤖 Healthcare Chatbot (Offline Version)

Welcome to the **Healthcare Chatbot** – a fully offline, intelligent chatbot designed to answer general healthcare questions using a large FAQ dataset. This project is built with **Python** and **Streamlit**, and does **not require any API calls**.  


## 🌟 Features

- **Offline Functionality:** No OpenAI API or external calls required.  
- **Large FAQ Dataset:** Handles 10,000+ questions for accurate responses.  
- **Fuzzy Matching:** Answers even if questions are phrased differently.  
- **Categories & Tags:** Faster and context-aware matching.  
- **Highlighted Keywords:** Important terms in answers are emphasized.  
- **Interactive Streamlit UI:**  
  - Colored chat bubbles for user & bot  
  - Collapsible answers for readability  
  - Display of question categories  

## 🗂️ Folder Structure
Healthcare_Chatbot/
│
├─ chatbot.py # Main Python script for chatbot
├─ faqs_large.json # Large FAQ dataset (10,000+ entries)
├─ generate_faqs.py # Script to generate the large FAQ dataset
├─ requirements.txt # Python dependencies
└─ README.md # Project description

## 💻 Installation & setup

1. **Clone the repository**

git clone https://github.com/PRABHU-tech/Healthcare_Chatbot.git
cd Healthcare_Chatbot

2.Install dependencies

pip install -r requirements.txt

3.Run the chatbot
streamlit run chatbot.py

4.Open your browser at the URL shown in Streamlit (usually http://localhost:8501) and start chatting!

📝 Example Questions
"I have a headache, what should I do?"

"Feeling very tired lately"

"My chest hurts, any advice?"

"How to reduce fever?"

The bot will provide the most relevant answer from the large FAQ dataset.

🛠️ Technology Stack
Python 3.8+ – Core programming language

Streamlit – Interactive web interface

FuzzyWuzzy – Fuzzy text matching for questions

JSON – FAQ dataset storage

🔐 Security
Offline Only: No sensitive data is sent over the internet.

API Key Protection: If using OpenAI API in the future, store keys in .env and do not commit them to GitHub.

✨ Future Improvements
Add voice input/output for hands-free interaction.

Implement search suggestions as the user types.

Categorize FAQs more deeply for specialized medical topics.

Highlight severity warnings for urgent symptoms.

📌 License
This project is open-source and available under the MIT License.

📫 Connect with Me
GitHub: PRABHU-tech

LinkedIn: [https://www.linkedin.com/in/prabhu-g-a34788267/]

