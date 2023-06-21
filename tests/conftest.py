from tests import get_async_session_test, AsyncTestSession
from revapp.models import Model, Review
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio
import os


def pytest_configure():
    asyncio.run(main())

async def main():
    await reset_and_synchronise_database()

    # create test review
    async with AsyncTestSession() as session, session.begin():
        reviews = [
            Review(user_id=1, reviewer_id=2, rating=4, review="Great product"),
            Review(user_id=1, reviewer_id=3, rating=5, review="Excellent product")
        ]
        session.add_all(reviews)
        await session.commit()


async def reset_and_synchronise_database():
    engine = create_async_engine(os.environ['DB_URI'])
    async with engine.begin() as connection:
        await connection.run_sync(Model.metadata.drop_all) 
        await connection.run_sync(Model.metadata.create_all)
    await engine.dispose()
