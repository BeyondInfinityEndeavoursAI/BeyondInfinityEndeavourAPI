from fastapi import FastAPI, Request, HTTPException
import hashlib

app = FastAPI()

# Hash your secret key for security
def hash_key(secret):
    return hashlib.sha256(secret.encode()).hexdigest()

API_KEY = hash_key("Usnotthem") # Your secret key, now hashed

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    key_header = request.headers.get("x-api-key")
    if not key_header or hash_key(key_header) != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await call_next(request)

@app.get("/")
def read_root():
    return {"message": "Beyond Infinity API is active!"}

@app.get("/ai")
def ai_status():
    return {"status": "AI cognition module running"}

@app.get("/ai/vision")
def ai_vision():
    return {"message":"Quantum Twin Vision: 7% Global Market Control"}
