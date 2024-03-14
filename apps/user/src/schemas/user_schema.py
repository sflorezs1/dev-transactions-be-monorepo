from pydantic import BaseModel, EmailStr
import uuid  

class UserCreate(BaseModel):
    id: uuid.UUID  
    name: str 
    email: EmailStr
    cedula: int
    address: str  
    operatorId: str
    operatorName: str