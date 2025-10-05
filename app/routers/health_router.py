from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/live")
def liveness():
    return {"status": "ok"}

@router.get("/ready")
def readiness():
    # extend with DB/ping checks if needed
    return {"status": "ready"}
