from flask import Flask, request, jsonify
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM  # Updated import
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

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

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)