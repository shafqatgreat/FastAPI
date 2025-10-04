from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr, constr, conint, HttpUrl, field_validator, model_validator
from datetime import date
from fastapi.middleware.cors import CORSMiddleware
import re

app = FastAPI(title="FastAPI Validation Examples")


# ================================
# 1️⃣ Basic Field Validation
# ================================
class BasicUser(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    email: EmailStr

@app.post("/basic-user")
def create_basic_user(user: BasicUser):
    return {"msg": "✅ Basic validation passed", "user": user}

# ================================
# 2️⃣ Advanced Field Types & Constraints
# ================================
class Product(BaseModel):
    
    
    class Product(BaseModel):
    name: constr(min_length=3, regex="^[a-zA-Z ]+$")
    quantity: conint(gt=0, lt=1000)
    website: HttpUrl
    
    
    name: constr(min_length=3)
    quantity: conint(gt=0, lt=1000)
    website: HttpUrl
    
    # Custom validation for name (only letters and spaces)
    @field_validator("name")
    def validate_name(cls, v):
        if not re.match(r"^[a-zA-Z ]+$", v):
            raise ValueError("Name must contain only letters and spaces")
        return v

@app.post("/product")
def create_product(product: Product):
    return {"msg": "✅ Advanced validation passed", "product": product}

# ================================
# # 3️⃣ Cross-Field Validation
# ================================

class Booking(BaseModel):
    start_date: date
    end_date: date

    @model_validator(mode='after')
    def check_dates(self):
        if self.start_date>= self.end_date:
            raise ValueError("start_date must be before end_date")
        return self

@app.post("/booking")
def create_booking(booking: Booking):
    return {"msg": "✅ Booking dates validated", "booking": booking}


# ==============================================================
# 🔹Cross-field validation using @model_validator(mode="after")
# ==============================================================
# ✅ (mode='after')runs after the whole model is created, so you can check
# ✅ Validation logic lives inside the model
# ✅ reusable across multiple endpoints
# ✅ Runs before the endpoint executes unlike Manual validation inside Endpoint
# ✅ Good for validational relationships between fields


# =========================================
# # 4️⃣ Manual Validation Inside Endpoint
# =========================================

class RegisterUser(BaseModel):
    username: str
    email: EmailStr

@app.post("/register")
def register_user(user: RegisterUser):
    if user.username.lower()== "admin":
        raise HTTPException(400,detail="❌ Username admin is reserved")
    return {"msg": "✅ User Registered successfully", "user": user}

















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





# # ================================
# # 2️⃣ Advanced Field Types & Constraints
# # ================================
# class Product(BaseModel):
#     name: constr(min_length=3, regex="^[a-zA-Z ]+$")
#     quantity: conint(gt=0, lt=1000)
#     website: HttpUrl

# @app.post("/product")
# def create_product(product: Product):
#     return {"msg": "✅ Advanced validation passed", "product": product}


# # ================================
# # 3️⃣ Custom Field Validation
# # ================================
# class SecureUser(BaseModel):
#     username: str
#     password: str

#     @field_validator("password")
#     def password_strength(cls, v):
#         if len(v) < 8:
#             raise ValueError("Password must be at least 8 characters")
#         if not any(char.isdigit() for char in v):
#             raise ValueError("Password must include at least one number")
#         return v

# @app.post("/secure-user")
# def create_secure_user(user: SecureUser):
#     return {"msg": "✅ Password validated successfully", "user": user}


# ================================
# 4️⃣ Cross-Field Validation
# ================================
# class Booking(BaseModel):
#     start_date: date
#     end_date: date

#     @model_validator(mode='after')
#     def check_dates(self):
#         if self.start_date >= self.end_date:
#             raise ValueError("start_date must be before end_date")
#         return self

# @app.post("/booking")
# def create_booking(booking: Booking):
#     return {"msg": "✅ Booking dates validated", "booking": booking}


# # ================================
# # 5️⃣ Manual Validation Inside Endpoint
# # ================================
# class RegisterUser(BaseModel):
#     username: str
#     email: EmailStr

# @app.post("/register")
# def register_user(user: RegisterUser):
#     if user.username.lower() == "admin":
#         raise HTTPException(400, detail="❌ Username 'admin' is reserved")
#     return {"msg": "✅ User registered successfully", "user": user}


# # ================================
# # 6️⃣ Validation Outside Body (Headers / Tokens)
# # ================================
# VALID_TOKEN = "codingmavrick123"

# @app.get("/secure-endpoint")
# def secure_endpoint(token: str):
#     if token != VALID_TOKEN:
#         raise HTTPException(403, detail="❌ Invalid or unauthorized token")
#     return {"msg": "✅ Authorized", "data": "Here is your secure info"}
