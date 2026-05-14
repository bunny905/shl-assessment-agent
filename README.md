# SHL Assessment Recommendation Agent

A conversational AI-powered recommendation system built for the SHL AI Intern Take-Home Assignment.

## Overview

This project helps recruiters and hiring managers discover suitable SHL assessments through natural conversation instead of keyword-based filtering.

The system:
- Understands hiring requirements conversationally
- Recommends relevant SHL assessments
- Supports multi-turn conversations
- Handles refinement requests
- Rejects off-topic queries
- Uses semantic similarity search with embeddings

---

## Features

- FastAPI backend
- `/health` endpoint
- `/chat` endpoint
- Conversational recommendation workflow
- Semantic search using Sentence Transformers
- Cosine similarity ranking
- Multi-turn context handling
- Off-topic query guardrails
- Structured JSON responses
- Swagger API documentation

---

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- Scikit-learn
- Uvicorn
- Pydantic

---

## Project Structure

```bash
shl-assessment-agent/
│
├── app/
│   ├── main.py
│   ├── data/
│   ├── services/
│   ├── utils/
│   └── models/
│
├── requirements.txt
├── README.md
└── .gitignore