from pydantic import BaseModel

class ReviewBase(BaseModel):
    user_id: int
    reviewer_id: int
    rating: int
    review: str

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    rating: int
    review: str

class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True
