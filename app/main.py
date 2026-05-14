from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.services.embedding_recommender import semantic_recommend


app = FastAPI(
    title="SHL Assessment Recommendation Agent",
    description="Conversational AI agent for recommending SHL assessments based on hiring requirements.",
    version="1.0.0"
)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    latest_message = request.messages[-1].content.lower()

    full_conversation = " ".join(
        [message.content.lower() for message in request.messages]
    )

    vague_queries = [
        "i need an assessment",
        "hiring",
        "need test",
        "need assessment"
    ]

    off_topic_keywords = [
        "salary",
        "legal",
        "lawsuit",
        "weather",
        "movie",
        "sports",
        "politics",
        "cricket"
    ]

    for keyword in off_topic_keywords:

        if keyword in latest_message:

            return {
                "reply": "I can only assist with SHL assessment recommendations and related assessment queries.",
                "recommendations": [],
                "end_of_conversation": False
            }

    if latest_message in vague_queries:

        return {
            "reply": "Could you specify the role, skills, or experience level you are hiring for?",
            "recommendations": [],
            "end_of_conversation": False
        }

    recommendations = semantic_recommend(full_conversation)

    if recommendations:

        return {
            "reply": "Here are some recommended SHL assessments based on your requirements.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    return {
        "reply": "Could you provide more details about the role, required skills, or assessment preferences?",
        "recommendations": [],
        "end_of_conversation": False
    }