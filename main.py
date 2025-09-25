from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# A fixed token for demonstration

VALID_TOKEN = "codingmavricktoken123"

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






@app.get("/secure-data")
def get_secure_data(authorization: str = Header(default=None)):
    print("Authorization Header receieved:",authorization)

    #Check if client provide a token
    if authorization is None:
        raise HTTPException(status_code=401,detail="Token missing")
    
    if authorization != VALID_TOKEN:
        raise HTTPException(status_code=403,detail="Invalid token provided")
    
    #if token is valid
    if authorization== VALID_TOKEN:
        return {"staus": "Authorized", "data": "Here is secure token provided"}
    
























# from fastapi import FastAPI, Header, HTTPException
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # A fixed token for demonstration (in real apps, this comes from login or database)
# VALID_TOKEN = "codingmavricktoken123"
               


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

# @app.get("/secure-data")
# def get_secure_data(authorization: str = Header(default=None)):
#     print("Authorization header received:", authorization)

#     # Check if client provided a token
#     if authorization is None:
#         raise HTTPException(status_code=401, detail="Token missing")

#     # Compare with the valid token
#     if authorization != VALID_TOKEN:
#         raise HTTPException(status_code=403, detail="Invalid or unauthorized token")

#     # If token is correct
#     return {"status": "Authorized ✅", "data": "Here is your secure information!"}
