from fastapi import FastAPI
from pydantic import BaseModel
from mvg_production import MVGProduction, AIConfig, AIProvider

class QueryRequest(BaseModel):
    user_id: str = "default"
    query: str

app = FastAPI(title="MVG Production API")

# Initialize MVG with mock provider by default (no API key required)
ai_conf = AIConfig(provider=AIProvider.MOCK)
mvg = MVGProduction(ai_conf)

@app.post("/api/v1/respond")
def respond(req: QueryRequest):
    result = mvg.process_request(req.query, req.user_id)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("mvg_api:app", host="127.0.0.1", port=8000, reload=False)
