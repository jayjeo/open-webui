from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from openwebui_milvus_direct import search_obsidian_notes  # ⬅️ 당신의 기존 함수

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    limit: Optional[int] = 50
    threshold: Optional[float] = 0.44

@app.post("/search")
def search_endpoint(request: QueryRequest):
    try:
        results = search_obsidian_notes(
            query=request.query,
            limit=request.limit,
            threshold=request.threshold
        )
        return {"status": "ok", "results": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}
