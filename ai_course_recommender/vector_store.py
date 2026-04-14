from difflib import SequenceMatcher

class EndeeVectorStore:
    def __init__(self):
        self.vectors = []

    def add(self, text, metadata):
        self.vectors.append({
            "text": text.lower(),
            "metadata": metadata
        })

    def search(self, query, top_k=5):
        query = query.lower()
        scored = []

        for item in self.vectors:
            sim = SequenceMatcher(None, query, item["text"]).ratio()
            scored.append((sim, item["metadata"]))

        scored.sort(key=lambda x: x[0], reverse=True)

        return [x[1] for x in scored[:top_k]]