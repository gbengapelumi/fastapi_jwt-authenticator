from pydantic import BaseModel, Field, EmailStr





class UserSchema(BaseModel):
    fullname: str = Field(default = None)
    email: EmailStr = Field(default = None)
    password: str = Field(default = None)
    class Config:
        the_schema = {
            "user_demo":{
                "name" : "Gbenga",
                "email": "orim@gmail.com",
                "password":"123"
            }
        }
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default = None)
    password: str = Field(default = None)
    class Config:
        the_schema = {
            "user_demo":{
                "email": "orim@gmail.com",
                "password":"123"
            }
        }
