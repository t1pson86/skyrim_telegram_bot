from app.database.database import async_session
from app.database.database import User
from sqlalchemy import select, insert, update, delete


async def set_user(telegram_id): #поиск usera по id telegram, если такого нет, то просто добавляем его
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))

        if not user:
            session.add(User(telegram_id=telegram_id))
            await session.commit()

async def get_user(telegram_id): #поиск usera по id telegram, если такого нет, то просто добавляем его
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))


#БАЛАНС
async def take_coins(telegram_id, balance): #обновление баланса -
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(balance=user.balance - balance)
        await session.execute(stmt)
        await session.commit()

async def add_coins(telegram_id, balance): #обновление баланса +
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(balance=user.balance + balance)
        await session.execute(stmt)
        await session.commit()



#ЗДОРОВЬЕ
async def take_health(telegram_id, health): #обновление здоровья -
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(health=user.health - health)
        await session.execute(stmt)
        await session.commit()

async def plus_health(telegram_id, health): #обновление здоровья +
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(health=user.health + health)
        await session.execute(stmt)
        await session.commit()

#Сила
async def plus_damage(telegram_id, damage): #обновление силы +
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(damage=user.damage + damage)
        await session.execute(stmt)
        await session.commit()

async def minus_damage(telegram_id, damage): #обновление силы -
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(damage=user.damage - damage)
        await session.execute(stmt)
        await session.commit()



#ЗАЩИТА
async def plus_protection(telegram_id, protection): #обновление защиты +
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(protection=user.protection + protection)
        await session.execute(stmt)
        await session.commit()

async def minus_protection(telegram_id, protection): #обновление защиты -
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(protection=user.protection - protection)
        await session.execute(stmt)
        await session.commit()

async def get_a_armor(telegram_id, armor): #запись доспеха в бд
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(armor=user.armor.replace('', armor))
        await session.execute(stmt)
        await session.commit()

async def clear_a_armor(telegram_id): #удаление записи из бд (доспех)
    async with async_session() as session:
        stmt = update(User).filter(User.telegram_id == telegram_id).values(armor='')
        await session.execute(stmt)
        await session.commit()


#LVL+opit
async def plus_experience(telegram_id, experience): #добавление опыта
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(experience=user.experience + experience)
        await session.execute(stmt)
        await session.commit()

async def defoult_exp(telegram_id): #добавление опыта
    async with async_session() as session:
        stmt = update(User).filter(User.telegram_id == telegram_id).values(experience=0)
        await session.execute(stmt)
        await session.commit()

async def up_lvl(telegram_id): #добавление lvl
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(lvl=user.lvl + 1)
        await session.execute(stmt)
        await session.commit()


#WORK PLACE
async def get_a_job(telegram_id, work_place): #устроиться на работу
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(work_place=user.work_place.replace('', work_place))
        await session.execute(stmt)
        await session.commit()

async def clear_a_job(telegram_id): #отчистить список работы
    async with async_session() as session:
        stmt = update(User).filter(User.telegram_id == telegram_id).values(work_place='')
        await session.execute(stmt)
        await session.commit()

#Добавление орудия в БД
async def get_a_gun(telegram_id, gun): #добавление орудия
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(gun=user.gun.replace('', gun))
        await session.execute(stmt)
        await session.commit()

async def clear_a_gun(telegram_id): #удаление орудия
    async with async_session() as session:
        stmt = update(User).filter(User.telegram_id == telegram_id).values(gun='')
        await session.execute(stmt)
        await session.commit()

#Добавление новой фермы в бд и обновление продукции
async def get_a_farm(telegram_id, farm): #добавление фермы
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(farm=user.farm.replace('', farm))
        await session.execute(stmt)
        await session.commit()

async def state_lvl_farm_lvl(telegram_id, farm_lvl): #обновление уровня фермы
    async with async_session() as session:
        stmt = update(User).filter(User.telegram_id == telegram_id).values(farm_lvl=farm_lvl)
        await session.execute(stmt)
        await session.commit()

async def farm_food_update(telegram_id, food_count): #обновление баланса от еды
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(balance = user.balance + food_count).values(farm_food=0)
        await session.execute(stmt)
        await session.commit()

async def updt_food_count(telegram_id, food_count): #обновление кол-во продукции на ферме
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        stmt = update(User).filter(User.telegram_id == telegram_id).values(farm_food = user.farm_food + food_count)
        await session.execute(stmt)
        await session.commit()


async def delete_farm(telegram_id): #удаление фермы
    async with async_session() as session:
        stmt = update(User).filter(User.telegram_id == telegram_id).values(farm='').values(farm_lvl=0).values(farm_food=0)
        await session.execute(stmt)
        await session.commit()