DOMAIN_MAP = {
    "cloud": ["cloud", "aws", "azure", "devops", "docker", "kubernetes"],
    "machine learning": ["machine learning", "ml", "ai", "deep learning"],
    "python": ["python", "oop", "scripting", "automation"],
    "data science": ["data science", "pandas", "numpy", "statistics"],
    "web": ["html", "css", "javascript", "frontend"]
}

KEY_MAP = {
    "ml": ["machine learning", "ml", "ai"],
    "python": ["python"],
    "data science": ["data science", "pandas", "numpy"],
    "web": ["web", "html", "css", "javascript"],
    "cloud": ["cloud", "aws", "azure"]
}

def extract_level(query):
    q = query.lower()

    if "beginner" in q or "basic" in q or "start" in q:
        return "Beginner"

    if "intermediate" in q:
        return "Intermediate"

    if "advanced" in q:
        return "Advanced"

    return None


def expand_query(query):
    q = query.lower()
    tokens = set()

    for key, values in KEY_MAP.items():
        if key in q:
            tokens.update(values)

    tokens.update(q.split())  # fallback

    return tokens


def score(query, course):
    tokens = expand_query(query)

    text = (
        course["title"] + " " +
        course["description"] + " " +
        " ".join(course["tags"])
    ).lower()

    sc = 0

    for t in tokens:
        if t in text:
            sc += 1

    sc += course["rating"] / 10

    return round(sc, 2)

def detect_domain(query):
    q = query.lower()

    for domain, keywords in DOMAIN_MAP.items():
        if any(k in q for k in keywords):
            return domain

    return None