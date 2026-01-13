# Hybrid Log Classification System

This project is my personal implementation of a **hybrid log classification framework**, designed to handle a variety of log patterns efficiently. By combining multiple classification methods, this system ensures flexibility, accuracy, and robustness when processing logs with different complexities.

---

## Classification Approaches

I implemented three complementary approaches to classify logs:

1. **Regular Expressions (Regex)**  
   - Handles simple and predictable log patterns.  
   - Useful for well-defined logs that follow consistent rules.

2. **Sentence Transformer + Logistic Regression**  
   - Handles complex patterns when there is enough labeled data.  
   - Converts log messages into embeddings using Sentence Transformers and classifies them using Logistic Regression.

3. **Large Language Model (LLM)**  
   - Provides a fallback or complementary approach for complex or poorly-labeled logs.  
   - Useful when training data is limited or patterns are highly variable.

---

## Project Structure

Here’s how I organized the project:

training/ --> Training scripts for Regex and Sentence Transformer + Logistic Regression models
models/ --> Saved models, including embeddings and classifiers
resources/ --> Example files, CSVs, images, and other resources
server.py --> FastAPI server for log classification

yaml
Copy code

---

## Setup Instructions

1. **Install Dependencies**  
   Make sure Python is installed. Then install the required packages:

   ```bash
   pip install -r requirements.txt
(If you run into missing dependencies like python-multipart, install it separately:)

bash
Copy code
pip install python-multipart
Start the FastAPI Server

bash
Copy code
uvicorn server:app --reload
Access the API endpoints at:

Main endpoint: http://127.0.0.1:8000/

Swagger docs: http://127.0.0.1:8000/docs

ReDoc docs: http://127.0.0.1:8000/redoc

How to Use
Upload a CSV file with logs to the FastAPI endpoint.

CSV must include the columns:

source

log_message

The API will return a CSV with an added column target_label containing the predicted classification.

Notes
This project is my personal work and is intended for learning and experimentation.

It should not be used for commercial purposes without proper authorization.

Created by: Ahmed El-sayed