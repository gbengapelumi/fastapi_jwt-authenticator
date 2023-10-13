import uvicorn
from fastapi import FastAPI, Body
from model import UserSchema, UserLoginSchema
from jwt_handler import signJWT


users = []
app = FastAPI()

#For the Homepage
@app.get("/")
def home():
    return {"To sign up and Login" : "try the input_url/docs "}

#Creating a New User
@app.post("/user/signup", tags = ["User Sign up"])
def user_signup(user: UserSchema = Body(default = None)):
    users.append(user)
    return signJWT(user.email)

#Checks if a user is in the database(Users list)
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    
#User Login
@app.post("/user/login", tags = ["User Login"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error":"invalid login details!"
        }