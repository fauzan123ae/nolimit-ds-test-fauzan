# nolimit-ds-test-fauzan

---

# Project Overview
Proyek ini merupakan implementasi Natural Language Processing (NLP) untuk melakukan sentiment classification pada teks menggunakan Hugging Face Sentence Transformers dan machine learning classifier.

Model mengubah teks menjadi embedding vector menggunakan model dari Hugging Face, kemudian melakukan klasifikasi sentimen positive atau negative menggunakan Logistic Regression.

Project ini dibuat sebagai bagian dari NoLimit Indonesia Data Scientist Hiring Test.

---

# Task Type
Task yang dipilih pada tes ini adalah:
# A. Classification — Sentiment Analysis
Model mengklasifikasikan teks menjadi dua kategori:
* Positive
* Negative

---
  
# Dataset
Dataset yang digunakan adalah Sentiment Labelled Sentences Dataset dari UCI Machine Learning Repository.

Dataset terdiri dari 3000 kalimat yang berasal dari tiga sumber:

* Amazon product reviews
* IMDb movie reviews
* Yelp restaurant reviews

Setiap kalimat memiliki label:
* 1 = Positive
* 0 = Negative
  
Dataset Source:
UCI Machine Learning Repository
https://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences

---

# Project Structure

---

## 📁 Struktur Folder
```
nolimit-ds-test-fauzan
│
├── data
│   ├── amazon_cells_labelled.txt
│   ├── imdb_labelled.txt
│   └── yelp_labelled.txt
│
├── notebooks
│   └── sentiment_analysis.ipynb
│
├── src
│   ├── app.py
│   └── classifier.pkl
│
├── flowchart.png
├── requirements.txt
└── README.md
```
---

# Setup Instructions

# 1.Clone Repository
 
 ```
 git clone  https://github.com/fauzan123ae/nolimit-ds-test-fauzan.git
```

Masuk Ke Folder Project:
```
cd nolimit-ds-test-fauzan
```

# 2. Install Dependencies

install Library yang dibutuhkan menggunakan:

```
pip install -r requirements.txt
```

# 3. Run Notebook

untuk menjalankan proses training dan evaluasi model:

```
notebooks/sentiment_analysis.ipynb
```
Notebook berisi proses

* load dataset
* train-test split
* embedding generation
* model training
* model evaluation
* example prediction

# 4.Run Streamlit App
```
streamlit run src/app.py
```

# 5. Run Streamlit Deployment on Streamlit Cloud

```
https://nolimit-ds-test-fauzan-testt.streamlit.app/
```

---

# Model Used

Project ini menggunakan model dari Hugging Face Sentence Transformers untuk membuat text embeddings.

Embedding Model:

```
sentence-transformers/all-MiniLM-L6-v2
```

Model ini mengubah teks menjadi vector embeddings yang kemudian digunakan sebagai fitur untuk klasifikasi.

Model Klasifikasi yang digunakan:

```
Logistic Regression (Scikit-learn)
```

 Model dilatih menggunakan embedding vector untuk memprediksi sentimen teks.

 ---

# Author

Fauzan Fathin Zaky

Project ini dibuat untuk keperluan NoLimit Indonesia Data Scientist Hiring Test
