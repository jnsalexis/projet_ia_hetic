from fastapi import FastAPI, Query
from pydantic import BaseModel
from .rag import generate_response


app = FastAPI()

class QueryRequest(BaseModel):
    question: str
    use_rag: bool = False
    temperature: float = 0.7

@app.post("/ask")
async def ask_question(request: QueryRequest):
    response = generate_response(
        question=request.question,
        use_rag=request.use_rag,
        temperature=request.temperature
    )
    return {"response": response}
