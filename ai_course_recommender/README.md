# 🎓 AI Course Recommendation System (Semantic + Vector-Based)

An intelligent AI-powered course recommendation system that suggests personalized learning paths based on user interests using semantic similarity, domain detection, and hybrid ranking logic.

It ensures **relevant and structured learning paths** for users like Python Developers, Cloud Engineers, Machine Learning learners, and Data Scientists while filtering irrelevant courses.

---

# ⚙️ How It Works

### 1️⃣ User Intent Detection
- Detects domain (Python / Cloud / ML / Data Science / Web)
- Detects learning level (Beginner / Intermediate / Advanced)

---

### 2️⃣ Domain Filtering
- Uses keyword-based mapping (`DOMAIN_MAP`)
- Removes unrelated courses before ranking

---

### 3️⃣ Semantic Search (Endee Vector Store)
- Each course is stored as a text-based representation
- Query is matched using similarity scoring (`SequenceMatcher`)
- Retrieves most relevant courses

---

### 4️⃣ Hybrid Ranking
Final score is calculated using:
- Course rating
- Semantic similarity
- Level match boost
- Rank position boost

---

# 🧠 System Architecture
User Query
↓
Streamlit UI (app.py)
↓
NLP Processing (utils.py)
├── Domain Detection
├── Level Extraction
↓
Domain Filtering (DOMAIN_MAP)
↓
Vector Search (vector_store.py - Endee)
↓
Ranking Engine (recommender.py)
↓
Final Course Recommendations
↓
Streamlit UI Display


---

# 🧪 How Endee is Used

Endee Vector Store is a lightweight semantic search engine used in this project.

### 📌 1. Indexing
- Each course is stored as: `title + description`

### 📌 2. Storage
- Saves course text + metadata (level, rating, website)

### 📌 3. Similarity Search
- Compares query with stored courses
- Uses similarity scoring to rank results

### 📌 4. Top-K Retrieval
- Returns top 5–6 most relevant courses

---

# 🏗️ Project Structure
ai-course-recommender/
│
├── app.py # Streamlit UI
├── recommender.py # Recommendation engine
├── dataset.py # Course dataset
├── utils.py # NLP utilities
├── vector_store.py # Endee search engine


---

# 🛠️ Tech Stack

- Python 🐍
- Streamlit 🎨
- Custom Vector Store (Endee)
- Difflib (Similarity matching)
- Rule-based NLP

---

# 📦 Features

✔ Semantic course matching  
✔ Domain-based filtering  
✔ Level detection  
✔ Role-aware recommendations  
✔ Hybrid ranking system  
✔ Clean UI with Streamlit  
✔ Lightweight (no heavy ML models)

---

# 📊 Sample Output

![Description](images/Course recommendation.png)
