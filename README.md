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

