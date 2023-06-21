from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os


async def get_async_session_test():
    engine = create_async_engine(os.environ['DB_URI'])
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield async_session
    finally:
        await engine.dispose()

class AsyncTestSession:
    URI = os.environ['DB_URI']

    async def __aenter__(self):
        self.engine = create_async_engine(self.URI) # used for patching URI for demo database # TODO: is there another way?
        async_session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)
        return async_session()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.engine.dispose()
