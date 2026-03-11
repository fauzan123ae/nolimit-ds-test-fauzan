import streamlit as st
from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

with open("src/classifier.pkl", "rb") as f:
    classifier = pickle.load(f)

st.title("Sentiment Analysis App")

text = st.text_area("Enter text")

if st.button("Predict"):

    embedding = model.encode([text])
    prediction = classifier.predict(embedding)

    if prediction[0] == 1:
        st.success("Positive Sentiment")
    else:
        st.error("Negative Sentiment")