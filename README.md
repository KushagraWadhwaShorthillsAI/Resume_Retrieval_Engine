# 🔎 Resume Retrieval Engine 

A powerful, Streamlit-based HR tool that enables intelligent resume search using advanced **Boolean logic** and custom **text normalization** techniques. Designed for recruiters and HR teams to efficiently filter candidate resumes stored in MongoDB using keywords, multi-word phrases, and logical expressions.

---

## 🚀 Features

* ✅ Boolean Search: Supports `AND`, `OR`, and parentheses `( )`
* ✅ Phrase Matching: Detects multi-word skills like `"Machine Learning"` or `HuggingFace`
* ✅ Intelligent Normalization:

  * Splits **CamelCase** (e.g., `HuggingFace` → `hugging face`)
  * Injects **merged bigrams** (`huggingface`) and **split halves** for fuzzy match
  * Strips emails, URLs, punctuation, and excess whitespace
* ✅ MongoDB Integration: Retrieves and filters resumes stored in your database
* ✅ Streamlit UI: User-friendly interface with card and table views
* ✅ Realtime Search Feedback with progress bar and formatted results

---

## 🧠 Boolean Search Guide

| Expression                                    | Behavior                               |
| --------------------------------------------- | -------------------------------------- |
| `Python`                                      | Matches any resume containing "Python" |
| `Python AND Django`                           | Both terms must be present             |
| `Java OR Python`                              | Either term can be present             |
| `(Java OR Python) AND (AWS OR Azure)`         | Grouped expressions                    |
| `"Machine Learning"`                          | Exact phrase match                     |
| `MachineLearning` or `(Machine AND Learning)` | Same as above                          |

**Multi-word Skills Handling**:

* You can write them as:

  * `MachineLearning`, `machinelearning`
  * `"Machine Learning"` (quoted)
  * `(Machine AND Learning)` (Boolean logic)

---

## 🧱 Architecture

```
MongoDB ↔ Resume Loader
             ↓
         JSON Flattener
             ↓
     🔄 Text Normalizer
             ↓
   Boolean Search Evaluator
             ↓
       ✅ Matching Results
             ↓
         Streamlit UI
```

---

## 🛠️ How to Run

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Set up MongoDB config** in `config.py`:

```python
MONGO_URI = "your_connection_string"
MONGO_DB_NAME = "your_db"
MONGO_COLLECTION_NAME = "your_collection"
```

3. **Run the Streamlit app**

```bash
streamlit run final_retriever_2.py
```

---

## 📄 File Structure

```
final_retriever_2.py      # Main Streamlit app and Boolean logic
config.py                 # MongoDB credentials
requirements.txt          # Required libraries
```

---

## 💡 Future Enhancements

* Vector-based semantic search integration.
* Advanced filtering (experience range, education level, location)
* Export matching results to CSV
* Authentication for multi-user support
* Handling Natural Language Queries.
* N8N Automated Integration.

---

