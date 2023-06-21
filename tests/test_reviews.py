import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from revapp import app
from revapp.dependencies import get_async_session
from revapp.models import Review as ReviewModel
from revapp.schemas import Review, ReviewCreate, ReviewUpdate
from unittest import IsolatedAsyncioTestCase


class ReviewIntegrationTest(IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = AsyncClient(app=app, base_url="http://test")

    async def tearDown(self):
        await self.client.close()

    async def test_read_review_existing(self):
        review_id = 1

        response = await self.client.get(f"/api/reviews/{review_id}")

        self.assertEqual(response.status_code, 200)

    async def test_read_review_not_found(self):
        review_id = 100

        response = await self.client.get(f"/api/reviews/{review_id}")

        self.assertEqual(response.status_code, 404)

    async def test_read_reviews(self):
        response = await self.client.get("/api/reviews")

        self.assertEqual(response.status_code, 200)
        reviews = response.json()
        self.assertIsInstance(reviews, list)

    async def test_create_review(self):
        review_data = {"user_id": 1, "reviewer_id": 2, "rating": 4, "review": "Great product"}

        response = await self.client.post("/api/reviews", json=review_data)

        self.assertEqual(response.status_code, 200)
        review = response.json()
        self.assertIsInstance(review, dict)
        self.assertEqual(review["user_id"], review_data["user_id"])
        self.assertEqual(review["reviewer_id"], review_data["reviewer_id"])
        self.assertEqual(review["rating"], review_data["rating"])
        self.assertEqual(review["review"], review_data["review"])

    async def test_update_review_existing(self):
        review_id = 1
        updated_review_data = {"rating": 5, "review": "Excellent product"}

        response = await self.client.put(f"/api/reviews/{review_id}", json=updated_review_data)

        self.assertEqual(response.status_code, 200)

    async def test_update_review_not_found(self):
        review_id = 100
        updated_review_data = {"rating": 5, "review": "Excellent product"}

        response = await self.client.put(f"/api/reviews/{review_id}", json=updated_review_data)

        self.assertEqual(response.status_code, 404)

    async def test_delete_review_existing(self):
        review_id = 2

        response = await self.client.delete(f"/api/reviews/{review_id}")

        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(response_json['status'], 'success')

    async def test_delete_review_not_found(self):
        review_id = 100

        response = await self.client.delete(f"/api/reviews/{review_id}")

        self.assertEqual(response.status_code, 404)
