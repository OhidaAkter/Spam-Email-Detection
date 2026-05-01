# 📧 Spam Email Detector

A simple web app that checks if an email is spam or not. Just paste your email and click a button!

Live Link: [ https://spam-email-check.streamlit.app/ ]

---

## 🎯 What Does This Do?

You paste an email → Click "Check Email" → It tells you if it's **spam** or **legitimate**

That's it! Simple as that. 

---

## 🖥️ How It Looks

- A clean email app style interface
- A text box where you paste the email
- A button to check it
- Red message if spam 🚨
- Green message if legitimate ✅

---

## Problems I Faced and How I Solved Them

Building this project was not smooth! I ran into two big problems:

---

### Problem 1 — Wrong Dataset ❌

**What happened:**
I started with the **UCI SMS Spam Collection Dataset** from Kaggle. It had 5,572 SMS text messages. The model trained on it and got 97% accuracy — which looked great!

But when I tested it with a real phishing email like this:
> *"Our system detected unauthorized access to your email account. Your account has been temporarily locked. Click the link below to verify your identity within 24 hours or your account will be permanently terminated."*

The model said it was a **legitimate email!** 

**Why did this happen?**
The model was trained on SMS messages like *"Win a free iPhone! Click here!"* — short and obvious spam. It never saw professional phishing emails with formal language, so it had no idea they were spam.

**How I fixed it:**
I switched to the **Email Spam Classification Dataset** by Balaka Biswas on Kaggle. This dataset has 5,172 **real emails** — not SMS messages. After training on this dataset, the model could now detect phishing emails correctly! ✅

---

### Problem 2 — Random Forest Too Aggressive ❌

**What happened:**
After switching to the new dataset, I tried different algorithms to get the best accuracy. Random Forest gave **97.77% accuracy** — the highest! So I used it.

But when I tested the web app with a completely normal email like:
> *"Hi Sarah, I wanted to follow up on our meeting scheduled for tomorrow at 10am. Please bring the quarterly report."*

The model said it was **SPAM!** 

It was marking **every single email as spam** — even obviously normal ones!

**Why did this happen?**
Random Forest is a very powerful algorithm. It was too aggressive and too strict — it saw any word it wasn't sure about and immediately called it spam. It was like a security guard who stops everyone from entering, even the regular employees!

**How I fixed it:**
I switched to **Naive Bayes** — a simpler algorithm that is specifically designed for word count data like emails. Even though the accuracy dropped slightly to 95.45%, it now correctly identifies both spam and legitimate emails. A slightly lower accuracy with correct behavior is much better than high accuracy with wrong behavior! ✅

---

## 📊 Final Results

| | First Try | Second Try | Final Version |
|---|---|---|---|
| Dataset | SMS messages | Real emails | Real emails |
| Algorithm | Naive Bayes | Random Forest | Naive Bayes |
| Accuracy | 97.57% | 97.77% | 95.45% |
| Phishing detection | ❌ Failed | ✅ Works | ✅ Works |
| Normal email detection | ✅ Works | ❌ Failed | ✅ Works |

---

## 🛠️ What I Used

- **Python** — programming language
- **Pandas** — to load and work with the dataset
- **Scikit-learn** — to build the ML model
- **NLTK** — to clean the email text
- **Streamlit** — to build the web interface
- **Pickle** — to save the trained model

---

## 📁 Files in This Project

```
Spam Email Detection/
│
├── spam_detection.ipynb   ← where the model is trained
├── main.py                ← Main Web Page
├── emails.csv             ← the dataset used for training
├── spam_model.pkl         ← the saved trained model
├── feature_columns.pkl    ← the saved word list
└── README.md              ← this file
```

---

## ⚙️ How to Run This on Your Computer

### Step 1 — Download the project
```bash
git clone https://github.com/yourusername/spam-email-detection.git
cd spam-email-detection
```

### Step 2 — Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3 — Install the required packages
```bash
pip install pandas numpy scikit-learn nltk streamlit
```

### Step 4 — Run the web app
```bash
streamlit run main.py
```

### Step 5 — Open your browser
A browser window will open automatically. Paste any email and click **Check Email**!

---

## 🧠 How It Works (Simple Version)

1. The model was trained on 5,172 real emails
2. It learned which words appear more in spam vs normal emails
3. When you paste a new email, it counts the words
4. It compares those words with what it learned
5. It gives you the result — spam or not!

---

## 📦 Dataset

Dataset used: [Email Spam Classification Dataset](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) from Kaggle

---

## 💡 What I Learned

- A high accuracy number does not always mean a good model
- The dataset is more important than the algorithm
- A simpler algorithm sometimes works better than a complex one
- Always test your model with real examples, not just accuracy numbers

---

## 👨‍💻 About

This is my first machine learning project. I built it to learn how ML works in real life — from training a model to building a web app around it.

Feel free to use it, improve it, or ask me anything! 😊
