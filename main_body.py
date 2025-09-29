from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

VALID_TOKEN = "codingmavrick123"


# Allow only your frontend (simple HTML file on localhost)
origins = [
    "http://127.0.0.1:5500",  # if you serve HTML via VSCode Live Server
    "http://localhost:5500",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allow all origins 👈 frontend domains
    allow_credentials=True,
    allow_methods=["*"],         # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],         # allow all headers (Authorization, Content-Type, etc.)
)



# Request body Model
class AuthRequest(BaseModel):
    token: str
# Pydantic Model for Profile info

class Profile(BaseModel):
    name: str
    email: EmailStr
    age: int

@app.post("/secure-data-body")
def get_secure_data(auth:AuthRequest):
    print("Token received in body:", auth.token)

    if auth.token != VALID_TOKEN:
        raise HTTPException(status_code=403,detail="Invalid or unauthorized token")
    
    return {"status":"Authorized","data":"Here is your secure information"}


@app.post("/profile")
def create_profile(profile: Profile):
    print("Received profile:", profile)

    return {
        "status": "Profile received",
        "data":
            {
                "name": profile.name,
                "email": profile.email,
                "age": profile.age
            }
    }

















