from pydantic import BaseModel
from typing import Optional
import constants.vote_constants as VOTE

"""
Data Access Object (DAO) schema for Votes in Firebase.
"""
class Vote(BaseModel):
    id: str  # Primary Key
    candidate_id: str  # Foreign Key reference to candidates
    precinct_id: str  # Foreign Key reference to precincts
    barangay_id: str  # Foreign Key reference to barangays
    votes_count: int
    updated_at: Optional[str] = None

# TODO: Add collection reference

# Create Vote
def create_vote(vote: Vote):
    raise NotImplementedError

# Read Vote
def get_vote(vote_id: str):
    raise NotImplementedError

# Update Vote
def update_vote(vote_id: str, update_data: dict):
    raise NotImplementedError

# Delete Vote (Soft Delete)
def delete_vote(vote_id: str):
    raise NotImplementedError

# Delete Vote (Hard Delete)
def delete_vote_hard(vote_id: str):
    raise NotImplementedError
