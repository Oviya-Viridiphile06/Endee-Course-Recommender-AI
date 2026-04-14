# 📚 AI Course Recommendation System (Semantic + Vector Based)

An intelligent AI-powered course recommender system that suggests personalized learning paths based on user interest using:

- Semantic similarity search (Endee Vector Store abstraction)
- Domain-aware filtering
- Level detection (Beginner / Intermediate / Advanced)
- Hybrid ranking system (rating + relevance + ranking boost)
- Streamlit-based interactive UI

---

# 🚀 Features

## 🔹 Smart Course Recommendation
Finds relevant courses based on meaning, not just keywords.

## 🔹 Domain Detection
Automatically detects domains:
- Python
- Cloud
- Machine Learning
- Data Science
- Web Development

## 🔹 Level Awareness
Supports:
- Beginner
- Intermediate
- Advanced

## 🔹 Hybrid Ranking System
Final ranking uses:
- Course rating
- Semantic similarity
- Level match boost
- Position-based boost

## 🔹 Beautiful UI (Streamlit)
- 3-column responsive layout
- Modern card UI
- Clean course presentation
- Direct “Visit Course” links

---

# 🏗️ Project Structure
ai-course-recommender/
│
├── app.py # Streamlit UI
├── recommender.py # Core recommendation engine
├── dataset.py # Course dataset
├── utils.py # NLP utilities (domain + level detection)
├── vector_store.py # Endee-based semantic search engine