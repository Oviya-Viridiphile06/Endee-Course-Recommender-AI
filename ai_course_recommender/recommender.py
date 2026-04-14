from dataset import COURSES
from utils import extract_level, detect_domain, DOMAIN_MAP
from vector_store import EndeeVectorStore


class Recommender:

    def __init__(self):
        self.vector_db = EndeeVectorStore()

        for course in COURSES:
            text = course["title"] + " " + course["text"]
            self.vector_db.add(text, course)

    def recommend(self, query):

        level_filter = extract_level(query)
        domain = detect_domain(query)

        # STEP 1: DOMAIN FILTERING (STRICTER VERSION)
        if domain and domain in DOMAIN_MAP:
            keywords = DOMAIN_MAP[domain]

            filtered = []
            for c in COURSES:
                text = (c["title"] + " " + c["text"]).lower()

                # stronger match rule (must match at least 1 keyword)
                if any(k in text for k in keywords):
                    filtered.append(c)
        else:
            filtered = COURSES

        # STEP 2: VECTOR SEARCH ON FILTERED SET
        temp_db = EndeeVectorStore()

        for c in filtered:
            temp_db.add(c["title"] + " " + c["text"], c)

        retrieved = temp_db.search(query)

        results = []

        for idx, c in enumerate(retrieved):

            # BASE SCORE: rating normalized (IMPORTANT FIX)
            score = c["rating"] * 0.6

            # SEMANTIC RANK BOOST (position-aware)
            score += (len(retrieved) - idx) * 0.2

            # LEVEL MATCH BOOST
            if level_filter and c["level"].lower() == level_filter.lower():
                score += 1.2

            # HARD PENALTY: irrelevant role mismatch (NEW FIX)
            if domain == "python" and "devops" in c["title"].lower():
                score -= 1.5

            results.append({
                "rank": idx + 1,
                "title": c["title"],
                "description": c["text"],
                "level": c["level"],
                "rating": c["rating"],
                "website": c["website"],
                "score": round(score, 2)
            })

        # FINAL SORT
        results.sort(key=lambda x: x["score"], reverse=True)

        return results[:6]