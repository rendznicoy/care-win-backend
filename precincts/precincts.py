from pydantic import BaseModel
from typing import Optional
import constants.precincts_constants as PRECINCT

# TODO: Initialize Firestore Client

"""
Data Access Object (DAO) schema for Precincts in Firebase.
"""
class Precinct(BaseModel):
    admin_id: str # Foreign Key reference to corresponding Precinct Admin
    barangay_id: str # Foreign Key reference to corresponding Barangay
    id: str # Primary Key
    updated_at: Optional[str] = None

# TODO: Add collection reference

# Create Precinct
def create_precinct(precinct: Precinct):
    raise NotImplementedError

# Read Precinct
def get_precinct(precinct_id: str):
    raise NotImplementedError

# Update Precinct
def update_precinct(precinct_id: str, update_data: dict):
    raise NotImplementedError

# Delete Precinct (Soft Delete)
def delete_precinct(precinct_id: str):
    raise NotImplementedError

# Delete Precinct (Hard Delete)
def delete_precinct_hard(precinct_id: str):
    raise NotImplementedError