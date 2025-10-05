from fastapi import FastAPI
from app.routers import auth_router, health_router

app = FastAPI(title="FastAPI Live Starter", version="1.0")

# Include routes
app.include_router(health_router.router)
app.include_router(auth_router.router)

@app.get("/")
def root():
    return {"message": "Running Good!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
