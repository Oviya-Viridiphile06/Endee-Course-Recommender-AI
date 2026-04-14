from difflib import SequenceMatcher

COURSES = [
    {
        "title": "Python Programming Mastery",
        "text": "Python programming basics OOP scripting file handling automation",
        "level": "Beginner",
        "rating": 4.5,
        "roles": ["python_developer", "beginner_programmer"],
        "website": {
            "name": "freeCodeCamp",
            "link": "https://www.freecodecamp.org",
            "desc": "Free structured coding curriculum"
        }
    },
    {
        "title": "Advanced Python Development",
        "text": "Python decorators generators APIs automation multithreading real world backend projects",
        "level": "Advanced",
        "rating": 4.6,
        "roles": ["python_developer", "backend_developer"],
        "website": {
            "name": "GeeksforGeeks",
            "link": "https://www.geeksforgeeks.org",
            "desc": "Coding + interview preparation"
        }
    },
    {
        "title": "Backend Development with Python (Django/FastAPI)",
        "text": "backend development APIs Django FastAPI authentication databases REST services",
        "level": "Intermediate",
        "rating": 4.7,
        "roles": ["python_developer", "backend_developer"],
        "website": {
            "name": "Udemy",
            "link": "https://www.udemy.com",
            "desc": "Project-based backend training"
        }
    },
    {
        "title": "Data Science Foundations",
        "text": "data science pandas numpy statistics visualization data cleaning analysis",
        "level": "Beginner",
        "rating": 4.4,
        "roles": ["data_scientist"],
        "website": {
            "name": "Kaggle Learn",
            "link": "https://www.kaggle.com/learn",
            "desc": "Hands-on ML & data science"
        }
    },
    {
        "title": "Machine Learning Core Concepts",
        "text": "machine learning regression classification clustering model evaluation algorithms",
        "level": "Intermediate",
        "rating": 4.7,
        "roles": ["data_scientist", "ml_engineer"],
        "website": {
            "name": "Coursera",
            "link": "https://www.coursera.org",
            "desc": "University-level structured learning"
        }
    },
    {
        "title": "Deep Learning Neural Networks",
        "text": "deep learning neural networks cnn rnn backpropagation ai models",
        "level": "Advanced",
        "rating": 4.8,
        "roles": ["ml_engineer", "ai_researcher"],
        "website": {
            "name": "Coursera",
            "link": "https://www.coursera.org",
            "desc": "Deep AI learning platform"
        }
    },
    {
        "title": "Cloud Computing Essentials",
        "text": "cloud computing aws azure virtualization distributed systems deployment",
        "level": "Beginner",
        "rating": 4.5,
        "roles": ["cloud_engineer"],
        "website": {
            "name": "AWS Training",
            "link": "https://aws.amazon.com/training",
            "desc": "Official AWS learning"
        }
    },
    {
        "title": "AWS Cloud Practitioner Fundamentals",
        "text": "cloud computing basics AWS services EC2 S3 IAM networking security fundamentals deployment concepts",
        "level": "Beginner",
        "rating": 4.6,
        "roles": ["cloud_engineer"],
        "website": {
            "name": "AWS Training",
            "link": "https://aws.amazon.com/training",
            "desc": "Official AWS beginner cloud certification path"
        }
    },
    {
        "title": "Advanced Cloud Architecture & Distributed Systems",
        "text": "cloud architecture microservices scalability load balancing distributed systems fault tolerance high availability Kubernetes AWS Azure GCP design patterns",
        "level": "Advanced",
        "rating": 4.8,
        "roles": ["cloud_engineer", "solutions_architect"],
        "website": {
            "name": "Coursera",
            "link": "https://www.coursera.org",
            "desc": "University-level cloud architecture training"
        }
    },
    {
        "title": "Cybersecurity Basics",
        "text": "cybersecurity encryption network security ethical hacking threats",
        "level": "Beginner",
        "rating": 4.5,
        "roles": ["cybersecurity_analyst"],
        "website": {
            "name": "Coursera",
            "link": "https://www.coursera.org",
            "desc": "Security fundamentals"
        }
    }
]

def get_best_website(query: str):
    q = query.lower()

    best = None
    best_score = 0

    for w in WEBSITES:
        score = 0

        for tag in w["tags"]:
            if tag in q:
                score += 2

        # fallback similarity boost
        score += SequenceMatcher(None, q, " ".join(w["tags"])).ratio()

        if score > best_score:
            best_score = score
            best = w

    return best if best else WEBSITES[0]