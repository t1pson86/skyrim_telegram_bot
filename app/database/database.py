from datetime import datetime
from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(
    url='sqlite+aiosqlite:///db.sqlite3'
)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id = mapped_column(BigInteger)
    status: Mapped[str] = mapped_column(default="спутник")
    health: Mapped[int] = mapped_column(default=100)
    damage: Mapped[int] = mapped_column(default=20)
    protection: Mapped[int] = mapped_column(default=100)
    lvl: Mapped[int] = mapped_column(default=0)
    experience: Mapped[int] = mapped_column(default=0)
    work_place: Mapped[str] = mapped_column(default='')
    farm: Mapped[str] = mapped_column(default='')
    farm_lvl: Mapped[int] = mapped_column(default=0)
    farm_food: Mapped[int] = mapped_column(default=0)
    gun: Mapped[str] = mapped_column(default='')
    armor: Mapped[str] = mapped_column(default='')
    balance: Mapped[int] = mapped_column(default=1000)
    last_farm_work_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
