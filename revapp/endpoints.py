from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from revapp import app
from revapp.dependencies import get_async_session
from revapp.models import Review as ReviewModel
from revapp.schemas import Review, ReviewCreate, ReviewUpdate

@app.get("/api/reviews/{review_id}", response_model=Review)
async def read_review(review_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(ReviewModel).filter_by(id=review_id))
    review = result.scalars().first()
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@app.get("/api/reviews", response_model=list[Review])
async def read_reviews(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(ReviewModel))
    reviews = result.scalars().all()
    return reviews

@app.post("/api/reviews", response_model=Review)
async def create_review(review: ReviewCreate, session: AsyncSession = Depends(get_async_session)):
    review_db = ReviewModel(**review.dict())
    session.add(review_db)
    await session.commit()
    return review_db

@app.put("/api/reviews/{review_id}")
async def update_review(review_id: int, review: ReviewUpdate, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(ReviewModel).filter_by(id=review_id))
    review_db = result.scalars().first()
    if review_db is None:
        raise HTTPException(status_code=404, detail="Review not found")

    await session.execute(
        update(ReviewModel).
        where(ReviewModel.id == review_id).
        values(**review.dict())
    )
    await session.commit()

    return {'status': 'success'}

@app.delete("/api/reviews/{review_id}")
async def delete_review(review_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(ReviewModel).filter_by(id=review_id))
    review = result.scalars().first()
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")

    await session.delete(review)
    await session.commit()

    return {'status': 'success'}
