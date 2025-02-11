from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import sqlite3
import pandas as pd

# Load data from SQLite database
def load_data():
    conn = sqlite3.connect('hospital.db')
    df = pd.read_sql_query("SELECT * FROM Schedules", conn)
    conn.close()
    return df.to_string()

# Vectorize data and store in FAISS
def vectorize_data():
    text = load_data()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(text)

    # Use Ollama embeddings
    embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")  # Replace "gemma2:2b" with your preferred Ollama model
    vectorstore = FAISS.from_texts(texts, embeddings)
    vectorstore.save_local("faiss_index")

# Run vectorization
vectorize_data()