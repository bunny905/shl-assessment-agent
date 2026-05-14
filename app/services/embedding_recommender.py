import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def load_assessments():

    with open("app/data/assessments.json", "r") as file:
        return json.load(file)


assessments = load_assessments()

assessment_texts = []

for assessment in assessments:

    combined_text = (
        assessment["name"] + " " +
        assessment["test_type"] + " " +
        " ".join(assessment["skills"])
    )

    assessment_texts.append(combined_text)


assessment_embeddings = model.encode(assessment_texts)


def semantic_recommend(user_query):

    query_embedding = model.encode([user_query])

    similarities = cosine_similarity(
        query_embedding,
        assessment_embeddings
    )[0]

    similarity_threshold = 0.35

    ranked_indices = similarities.argsort()[::-1]

    recommendations = []

    for index in ranked_indices[:5]:

        if similarities[index] < similarity_threshold:
            continue

        assessment = assessments[index]

        recommendations.append({
            "name": assessment["name"],
            "url": assessment["url"],
            "test_type": assessment["test_type"]
        })

    return recommendations