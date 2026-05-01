import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from datetime import datetime
import numpy as np

nltk.download('stopwords')

# Load saved model and feature columns
model = pickle.load(open('spam_model.pkl', 'rb'))
feature_columns = pickle.load(open('feature_columns.pkl', 'rb'))

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return words

def email_to_features(email_text):
    # Get words from email
    words = clean_text(email_text)
    
    # Create a vector of zeros for all 3000 features
    features = np.zeros(len(feature_columns))
    
    # Count each word that exists in our feature columns
    for word in words:
        if word in feature_columns:
            index = feature_columns.index(word)
            features[index] += 1
    
    return features.reshape(1, -1)

# Page config
st.set_page_config(page_title="Spam Email Detector", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');

    .main { background-color: #ffffff; }

    .block-container {
        padding-top: 60px !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #f0f2f8;
        padding-top: 0px !important;
    }

    .sidebar-top {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 5px 0 20px 0;
    }

    .compose-btn {
        background-color: #7b5ea7;
        color: white;
        padding: 12px 25px;
        border-radius: 25px;
        font-size: 15px;
        margin-bottom: 30px;
        display: inline-block;
    }

    .sidebar-item {
        padding: 10px 5px;
        font-size: 15px;
        color: #444;
        margin: 5px 0;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
    }

    .title-box {
        background-color: #f5c9a0;
        padding: 15px 40px;
        border-radius: 40px;
        font-size: 22px;
        font-weight: bold;
        color: #222;
        text-align: center;
        margin: 0 auto 8px auto;
        max-width: 600px;
    }

    .subtitle {
        text-align: center;
        color: #555;
        font-size: 15px;
        margin-bottom: 40px;
        font-family: 'Poppins', sans-serif;
    }

    .time-display {
        text-align: right;
        color: #888;
        font-size: 14px;
        margin-bottom: 5px;
        font-weight: bold;
        margin-top: -20px;
    }

    .stTextArea textarea {
        background-color: #ddeeff;
        border-radius: 15px;
        border: none;
        font-size: 15px;
        padding: 15px;
        font-family: 'Poppins', sans-serif;
    }

    .stTextArea textarea:focus {
        border: 2px solid #7b5ea7 !important;
        box-shadow: 0 0 0 2px rgba(123, 94, 167, 0.2) !important;
        outline: none !important;
    }

    .stTextArea > div:focus-within {
        border-color: #7b5ea7 !important;
        box-shadow: 0 0 0 2px rgba(123, 94, 167, 0.2) !important;
    }

    .stButton button {
        background-color: #7b5ea7;
        color: white;
        border-radius: 25px;
        padding: 10px 30px;
        font-size: 15px;
        border: none;
        display: block;
        margin: 0 auto;
    }

    .stButton button:hover {
        background-color: #5a3e8a;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-top">☰ Email</div>', unsafe_allow_html=True)
    st.markdown('<div class="compose-btn">✏️ Compose</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item"><span style="font-size:18px">🗂️</span> Inbox</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item"><span style="font-size:18px">⭐</span> Starred</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item"><span style="font-size:18px">🕐</span> Snoozed</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item"><span style="font-size:18px">📌</span> Important</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item"><span style="font-size:18px">📤</span> Sent</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item"><span style="font-size:18px">📝</span> Drafts</div>', unsafe_allow_html=True)

# Main content
st.markdown('<div class="title-box">🌐 Intelligent Spam Email Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Type or paste an email below to check if it\'s spam or not!</div>', unsafe_allow_html=True)

# Time
now = datetime.now().strftime("%a, %b %d, %I:%M %p")
st.markdown(f'<div class="time-display">🕐 {now}</div>', unsafe_allow_html=True)

# Text area
email_input = st.text_area("", height=200, placeholder="Paste your email text here...")

# Button centered
col1, col2, col3 = st.columns([1.2, 1, 1])
with col2:
    check = st.button("🔍 Check Email")

if check:
    if email_input.strip() == "":
        st.warning("⚠️ Please enter some email text!")
    else:
        features = email_to_features(email_input)
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.error("🚨 SPAM EMAIL DETECTED!")
        else:
            st.success("✅ This is a legitimate email!")