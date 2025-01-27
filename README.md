# Hospital RAG System

This project implements a Retrieval-Augmented Generation (RAG) system that 
processes an Excel sheet containing data for the Pain & Go hospital, including information on 
physicians, schedules, and pricelists. The system's role will be to answer user inquiries, such as 
the schedule of a specific doctor, the most appropriate doctor or specialty based on the question
It uses a Flask API, Streamlit UI, and SQLite database to answer user queries about doctor schedules.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/0Xuser100/AI-Powered-HIS-Customer-Services.git
   cd AI-Powered-HIS-Customer-Services
   ```

## Install dependencies
```bash
pip install -r requirements.txt
```
## Set up the database

```bash
python database.py
```

## Vectorize the data
```bash
python vectorization.py
```