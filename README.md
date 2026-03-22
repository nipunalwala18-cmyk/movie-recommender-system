# 🎬 Movie Recommender System

A content-based Movie Recommender System that suggests movies similar to the one you like. Built using Machine Learning, Streamlit, and TMDB API for posters.

---

## 🚀 Features

* 🔍 Search for any movie
* 🎯 Get top 5 similar movie recommendations
* 🖼️ Movie posters fetched dynamically using API
* ⚡ Fast similarity computation using preprocessed data
* 💻 Interactive UI built with Streamlit

---

## 🧠 How It Works

This project uses a **content-based filtering approach**:

* Movies are compared based on features like genres, keywords, cast, and crew
* A similarity matrix is created using cosine similarity
* When a user selects a movie, the system finds the most similar movies

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* Streamlit
* TMDB API

---

## 📁 Project Structure

```
📦 Movie-Recommender-System
├── app.py                 # Streamlit app
├── movies.pkl            # Movie dataset
├── similarity.pkl        # Similarity matrix
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/nipunalwala18-cmyk/movie-recommender-system.git
cd movie-recommender-system
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🔑 API Setup (TMDB)

1. Create an account on https://www.themoviedb.org/
2. Get your API key
3. Replace it in your code:

```python
api_key = "YOUR_API_KEY"
```

---

## 📸 Demo

* Select a movie from the dropdown
* Click **Recommend**
* Get top 5 similar movies with posters

---

## ⚠️ Note on Large Files

This project uses **Git LFS** to manage large `.pkl` files:

* `movies.pkl`
* `similarity.pkl`

Make sure Git LFS is installed before cloning:

```bash
git lfs install
git lfs pull
```

---

## 💡 Future Improvements

* 🎥 Add movie trailers
* ⭐ Show ratings & reviews
* 🔎 Add search autocomplete
* 📱 Improve mobile responsiveness
* 🤖 Switch to hybrid / collaborative filtering

---

## 🙌 Acknowledgements

* TMDB for movie data and posters
* Scikit-learn for ML tools
* Streamlit for UI framework

---

## 👨‍💻 Author

**Nipun Alwala**

---
