from pydantic import BaseModel
from typing import Optional
import constants.user_constants as USER

# TODO: Initialize Firestore Client

"""
Data Access Object (DAO) schema for Users in Firebase.
"""
class User(BaseModel):
    active: bool = True
    details: Optional[str] = None
    email: Optional[str] = None
    id: str
    name: str
    phone: Optional[str] = None
    photo_url: Optional[str] = None
    role: int  # 0: Precinct Admin, 1: Barangay Admin, 2: City Admin
    updated_at: Optional[str] = None

# TODO: Add collection reference

# Create User
def create_user(user: User):
    raise NotImplementedError

# Read User
def get_user(user_id: str):
    raise NotImplementedError

# Update User
def update_user(user_id: str, update_data: dict):
    raise NotImplementedError

# Delete User (Soft Delete)
def delete_user(user_id: str):
    raise NotImplementedError

# Delete User (Hard Delete)
def delete_user_hard(user_id: str):
    raise NotImplementedError