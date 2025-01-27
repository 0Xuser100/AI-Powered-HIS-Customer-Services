Here’s the updated `README.md` file with the `/insert` endpoint added to the **API Endpoints** section:

---

# Hospital RAG System

This project implements a Retrieval-Augmented Generation (RAG) system that processes an Excel sheet containing data for the Pain & Go hospital, including information on physicians, schedules, and pricelists. The system's role will be to answer user inquiries, such as the schedule of a specific doctor, the most appropriate doctor or specialty based on the question. It uses a Flask API, Streamlit UI, and SQLite database to answer user queries about doctor schedules.

---

## **Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/0Xuser100/AI-Powered-HIS-Customer-Services.git
   cd AI-Powered-HIS-Customer-Services
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python database.py
   ```

4. Vectorize the data:
   ```bash
   python vectorization.py
   ```

5. Run the Flask API:
   ```bash
   python app.py
   ```

6. Run the Streamlit UI:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## **API Endpoints**

### **POST /query**: Answer user queries
- **Description**: Accepts a user query and returns an answer based on the hospital's data.
- **Request Body**:
  ```json
  {
      "query": "What is Dr. Alice Smith's schedule?"
  }
  ```
- **Response**:
  ```json
  {
      "answer": "Dr. Alice Smith's schedule is Monday: 9 AM - 5 PM, Tuesday: 9 AM - 5 PM, Wednesday: 9 AM - 5 PM, Thursday: 9 AM - 5 PM, Friday: 9 AM - 5 PM, Saturday: Off, Sunday: Off."
  }
  ```

### **POST /insert**: Insert new records into the database
- **Description**: Inserts a new doctor's schedule into the database and updates the vector store.
- **Request Body**:
  ```json
  {
      "doctor_name": "Dr. Mahmoud",
      "monday": "10 AM - 6 PM",
      "tuesday": "10 AM - 6 PM",
      "wednesday": "10 AM - 6 PM",
      "thursday": "10 AM - 6 PM",
      "friday": "10 AM - 6 PM",
      "saturday": "Off",
      "sunday": "Off"
  }
  ```
- **Response**:
  ```json
  {
      "message": "Record inserted and vector database updated successfully"
  }
  ```

---

## **How to Run**

1. Run `database.py` to set up the database.
2. Run `vectorization.py` to vectorize the data.
3. Run `app.py` to start the Flask API.
4. Run `streamlit_app.py` to start the Streamlit UI.

---

## **Example Queries**

- "What is Dr. Alice Smith's schedule?"
- "When is Dr. John Brown available on Tuesday?"
- "Who is available on Friday?"

---

## **Example Insertion**

To insert a new doctor's schedule, send a POST request to the `/insert` endpoint with the following JSON payload:
```json
{
    "doctor_name": "Dr. Mahmoud",
    "monday": "10 AM - 6 PM",
    "tuesday": "10 AM - 6 PM",
    "wednesday": "10 AM - 6 PM",
    "thursday": "10 AM - 6 PM",
    "friday": "10 AM - 6 PM",
    "saturday": "Off",
    "sunday": "Off"
}
```

---

## **Notes**

- Ensure that the `hospital.db` database and the `Schedules` table exist before running the app. You can create the table using the following SQL command:
  ```sql
  CREATE TABLE Schedules (
      "Doctor Name" TEXT NOT NULL,
      "Monday" TEXT,
      "Tuesday" TEXT,
      "Wednesday" TEXT,
      "Thursday" TEXT,
      "Friday" TEXT,
      "Saturday" TEXT,
      "Sunday" TEXT
  );
  ```

- The `/insert` endpoint automatically updates the vector store after inserting a new record.

---
