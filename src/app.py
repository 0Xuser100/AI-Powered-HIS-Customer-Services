from flask import Flask, request, jsonify
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
import sqlite3

app = Flask(__name__)

# Load FAISS vectorstore with Ollama embeddings
embeddings = OllamaEmbeddings(model="gemma2:2b")  # Replace "gemma2:2b" with your preferred Ollama model
vectorstore = FAISS.load_local(
    "faiss_index", 
    embeddings, 
    allow_dangerous_deserialization=True  # Add this parameter
)

# Initialize Ollama LLM
llm = OllamaLLM(model="gemma2:2b")  # Replace "gemma2:2b" with your preferred Ollama model

# QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# API to answer user queries
@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({"error": "Query is required"}), 400

    result = qa_chain.run(query)
    return jsonify({"answer": result})

# API to insert new records into the database
@app.route('/insert', methods=['POST'])
def insert():
    data = request.json
    doctor_name = data.get('doctor_name')
    monday = data.get('monday')
    tuesday = data.get('tuesday')
    wednesday = data.get('wednesday')
    thursday = data.get('thursday')
    friday = data.get('friday')
    saturday = data.get('saturday')
    sunday = data.get('sunday')

    if not doctor_name:
        return jsonify({"error": "Doctor name is required"}), 400

    # Insert into SQLite database
    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Schedules ("Doctor Name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (doctor_name, monday, tuesday, wednesday, thursday, friday, saturday, sunday))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500
    finally:
        conn.close()

    # Re-vectorize the updated data
    try:
        from vectorization import vectorize_data
        vectorize_data()
    except ImportError:
        return jsonify({"error": "Vectorization module not found"}), 500
    except Exception as e:
        return jsonify({"error": f"Vectorization error: {e}"}), 500

    return jsonify({"message": "Record inserted and vector database updated successfully"})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)