from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

# database dependencies
async def get_async_session() -> AsyncSession:
    '''
    Async context manager for database session
    '''

    engine = create_async_engine(os.environ['DB_URI'])
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        async with async_session() as session, session.begin():
            yield session
    finally:
        await session.close()
        await engine.dispose()
