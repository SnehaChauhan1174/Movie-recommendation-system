# 🎬 Movie Recommendation System

## 📌 Overview

This project is a movie  recommendation system that suggests top 5 matched movies based on cosine similarity. It leverages NLP techniques and vector space models to compute similarity between entities, and uses a precomputed model file (`similarity.pkl`) for efficient results.

> ⚠️ Note: Due to GitHub's 100MB file limit, the `similarity.pkl` file is not included here. Please follow the instructions below to download it.

---

## 🍿 Features

- 🎯 Suggests movies based on input title
- 🧠 Uses NLP + cosine similarity on overview vectors
- 🚀 Fast recommendations with precomputed data
- 🎨 Simple Streamlit UI

## 🗂️ Project Structure

├── app.py # Streamlit app
├── movie-recomm.ipynb # Jupyter notebook
├── similarity.pkl # Large similarity matrix (not included)
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md # This file


## 🧪 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SnehaChauhan1174/Movie-recommendation-system.git
```

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### ▶️ Run the App Locally

streamlit run app.py

🧠 Technologies Used
Python
Streamlit
scikit-learn
Pandas
NumPy
NLP techniques (TF-IDF, cosine similarity)


This project demonstrates how simple NLP techniques and vector similarity can be used to build a content-based movie recommendation system. By combining Python, Streamlit, and scikit-learn, I created an interactive, real-time app that showcases the practical side of machine learning.
It can be easily extended or deployed, making it a solid foundation for more advanced recommendation engines.

👩‍💻 Author
Sneha Chauhan
📍 AI/ML Student
🔗 [LinkedIn](https://www.linkedin.com/in/sneha-chauhan-tech6119/)




