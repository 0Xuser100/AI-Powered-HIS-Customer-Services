# Hospital RAG System

This project implements a Retrieval-Augmented Generation (RAG) system that 
processes an Excel sheet containing data for the Pain & Go hospital, including information on 
physicians, schedules, and pricelists. The system's role will be to answer user inquiries, such as 
the schedule of a specific doctor, the most appropriate doctor or specialty based on the question
It uses a Flask API, Streamlit UI, and SQLite database to answer user queries about doctor schedules.

## **Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/0Xuser100/AI-Powered-HIS-Customer-Services.git
   cd AI-Powered-HIS-Customer-Services
   ```

## **Install dependencies**
```bash
pip install -r requirements.txt
```
## **Set up the database**

```bash
python database.py
```

## **Vectorize the data**
```bash
python vectorization.py
```

##  **Run the Flask API**
```bash
python app.py
```
## **Run the Streamlit UI**
```bash
streamlit run streamlit_app.py
```
## **API Endpoints**
#### POST /query: Answer user queries


---

### **How to Run**
1. Run `database.py` to set up the database.
2. Run `vectorization.py` to vectorize the data.
3. Run `app.py` to start the Flask API.
4. Run `streamlit_app.py` to start the Streamlit UI.

---

### **Example Queries**
- "What is Dr. Alice Smith's schedule?"
- "When is Dr. John Brown available on Tuesday?"
- "Who is available on Friday?"

---
