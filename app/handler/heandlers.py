from datetime import datetime, timedelta

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

import random
import asyncio
import time
from time import timezone


from app.dict_package.info_about import list_random
import app.database.requests as rq
from app.buttons.keyboards import (
                                main,
                                works_list,
                                eat_shop,
                                play,
                                live_on_work_place,
                                clear_a_list_gun,
                                clear_a_list_armor,
                                sell_a_farm,
                                up_farm_lvl,
                                up_farm_lvl_max,
                                shop_or_eat,
                                go_to_main,
                                shop_or_paupau,
                                mechy,
                                dospehy,
                                list_mechy,
                                list_bronya,
                                list_bronya_tyajelaya,
                                all_fermies,
                                list_my_fermies,                                                      
)

from app.database.database import async_session
from app.database.database import User
from sqlalchemy import select, update



router = Router()



random_money = list(range(10, 101)) # рандомные монеты
random_health = list(range(5, 81)) # рандомные хп
random_experience = list(range(1, 6)) # рандомные хп




@router.message(CommandStart())#Запись человека в БД + приветствие
async def start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f"""
🏰 Добро пожаловать в Skyrim Adventures! 🏰

Ты оказался в мире Скайрима, где тебя ждут:
⚔️ Захватывающие битвы с чудовищами
💰 Развитие ферм и бизнеса
🛡️ Эпические доспехи и оружие
📊 Прокачка персонажа до 15 уровня

Как начать:
1. Проверь свой *Профиль* 🧙‍♂️
2. Отправься в *Путешествие* 👣 за первой добычей
3. Загляни в *Таверну* 🛖 чтобы восстановить силы

Используй меню внизу для навигации.
Удачных приключений, драконорождённый!
""", reply_markup=main)



@router.message(F.text=='Профиль 🧙‍♂️') #профиль игрока
async def profile(message: Message):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == message.from_user.id))
        await message.answer(f"""
👤 Ваш профиль:

|-🙎‍♂Ваш ID -『 {message.from_user.id} 』
|
|-👑Статус -『 {user.status} 』
|
|-❤️Здоровье -『 {user.health} hp 』
|
|-⚔️Урон -『 {user.damage} hp 』
|
|-🛡Защита -『 {user.protection} 』
|
|-💪Уровень -『 {user.lvl} lvl 』
|
|-🍃Опыт -『 {user.experience} XP 』
|
|-💰Баланс -『 {user.balance} монет(-ы, -а) 』
|
|-💼Работа -『 {user.work_place} 』
|
|-🐾Ферма -『 {user.farm} 』
|
|-🐾Уровень Фермы -『 {user.farm_lvl} 』

🔎 СПИСОК СНАРЯЖЕНИЙ:

|- 🗡Оружие - 『 {user.gun} 』
|- 🎽Доспехи - 『 {user.armor} 』

    """)
        

@router.message(F.text=='Уровни 💫') #магазин вещей
async def shop(message: Message):
    await message.answer("""
1 до 2 — 35XP
2 до 3 — 60 XP
3 до 4 — 90 XP
4 до 5 — 135 ХР
5 ДО 6 — 160 ХР
6 ДО 7 — 195 ХР
7 ДО 8 — 240 ХР
8 ДО 9 — 290 XP
9 до 10 — 345 ХР
10 ДО 11 —  380 ХР
11 ДО 12 — 425 ХР
12 ДО 13 — 480 ХР
13 ДО 14 — 520 ХР
14 ДО 15 — 600 ХР
""", reply_markup=go_to_main)

@router.message(F.text=='Таверна 🛖') #магазин вещей
async def shop(message: Message):
    await message.answer('Таверна 🛖 (магазин)', reply_markup=shop_or_eat)


@router.message(F.text=='Главное меню 🔙') #главное меню
async def shop(message: Message):
    await message.answer('Главное меню', reply_markup=main)


@router.message(F.text=='Еда') #магазин еды
async def shop(message: Message):
    await message.answer("""
Яблочный пирог - + 30HP ( 50 золото)

Печёный картофель — 5HP (7 золото) 

Хлеб — 10HP (15 золото) 

Кусок козьего сыра — 40HP (60 золото) 

Пчелиный мёд — 25HP (40 золото)

Сладкий рулет — 50HP (70 золото) 

Жареная рыба-убийца — 80HP (120 золото)

‼️‼️ Доступ с 5-го уровня ‼️‼️

Тушенная говядина — + 120 HP ( 250 золото) 

Копустный суп — + 150  HP ( Золото 350 золото )

Вареная говядина — + 200 HP ( 500 Золото) 

Куригая грудка на гриле — + 280 HP ( 670 Золото ) 

‼️‼️ Доступ с 9-го уровня ‼️‼️

Лошадиный окорок — + 340 HP ( 760 Золото ) 

Стейк из мамонта — + 420 HP ( 860 Золото ) 

Жаркое из фазана — + 500 HP ( 1000 Золото ) 

‼️‼️ Доступ с 15 уровня ‼️‼️

Отбивная из оленины — + 600 HP ( 1350 золото ) 

Тушенная оленина — + 680 HP ( 1550 золото ) 

Стейк из лосося — + 750 HP ( 1800 Золото ) 

Тушеное мясо по-Хоркерски — 920 HP ( 2390 Золото ) 

Эльсвейрское фондю — 1110 HP ( 2750 Золото ) 

Ножки Грязевого краба — 1400 HP ( 3350 Золото )
                         
Внимание: чтобы востановить хп, вы должны купить, что-то из меню! Нажав на выбранный товар, вы автоматически его купите.
""", reply_markup=eat_shop)


@router.message(F.text=='Доспехи')
@router.message(F.text=='Обратно к списку доспехов 🔙')
async def shop(message: Message):
    await message.answer('Выберите категорию', reply_markup=dospehy)

@router.message(F.text=='Броня')
async def shop(message: Message):
    await message.answer("""
Список броней 🛡:

‼️‼️Доступно с 2 уровня‼️‼️  
                            
Ржавая железная броня — + 25 HP (400 золото) 

Меховая броня — + 50 HP ( 750 золото) 

Кожанная броня — + 85 HP (950 золото) 

Поношенная броня 110 HP ( 1100 золото) 

‼️‼️ Доступ с 5-го уровня ‼️‼️

Чешуйчатая броня — + 150 HP (1850 золото) 

Лёгкая имперская броня — +185 HP ( 2100 золото) 

Железная броня — + 215 HP ( 2400 золото)

Офицерская броня — + 260 HP ( 2650 золото) 

‼️‼️ Доступ с 9-го уровня ‼️‼️

Хитиновая броня — + 300 HP ( 2950 золото) 

Стеклянная броня — + 360 HP ( 3400 золото) 

Броня из драконей чешуи — + 400 HP ( 3750 золото)

Броня стража рассвета — + 500 HP ( 4300 золото)
""", reply_markup=list_bronya)
    
@router.message(F.text=='Тяжёлая броня')
async def shop(message: Message):
    await message.answer("""
Список тяжёлых броней 🛡:
                         
‼️‼️ Доступ с 13-го Уровня ‼️‼️

Броня из костей  — + 650 HP ( 7000 золото ) 

Тяжёлая хитиновая броня — + 850 HP ( 9500 золото ) 

Тяжёлая броня Фалмера — + 1000 HP ( 11000 золото) 

Закалённая броня Фалмера — 1250 HP ( 14500 золото) 

Броня из драконьих доспехов — + 1450 HP ( 17000 золото )

Даэдрическая броня — + 1800  HP ( 19500 золото )
""", reply_markup=list_bronya_tyajelaya)
    
# @router.message(F.text=='Уникальная броня')
# async def shop(message: Message):
#     await message.answer("""
# Список уникальных броней 🛡:

# ‼️‼️ Доступно с 15-го уровня ‼️‼️

# Древние доспехи Фалмеров — + 3000 HP + 55 защиты ( 120 рублей ) 

# Древние закутанные доспехи — + 5300 HP  + 80 защиты ( 210 рублей ) 

# Доспехи Старых богов — + 7500 HP + 130 защиты ( 315 рублей ) 

# Доспехи Ахзидала — + 9800 HP + 190 защиты ( 400 рублей ) 

# Набор доспехов гильдмастера — + 11 500 HP +  250 защиты ( 510 рублей ) 

# Доспехи Смертоносца — + 15 000 + 340 защиты ( 600 рублей )
# """, reply_markup=list_bronya_unic)
    


@router.message(F.text=='Оружие')
async def shop(message: Message):
    await message.answer('Выберите категорию', reply_markup=mechy)

@router.message(F.text=='Мечи')
@router.message(F.text=='Обратно к списку орудий 🔙')
async def shop(message: Message):
    await message.answer("""
Список "Мечей⚔️" :

‼️‼️Доступно с 2 уровня‼️‼️
                         
Ржавый клинок — + 5 урона (80 золото) 

Не заточенный железный меч — + 10 урона (120 золото) 

Железный меч — + 20 урона (170 золото) 

Доступ с 3-го уровня‼️

Стальной не заточенный меч — + 30 урона (300 золото) 

Имперакий меч — + 50 урона ( 550 золото) 

Стальной меч — + 70 урона ( 750 золото) 

Стальной двуручный меч — + 100 урона ( 900 золото) 

Орочьий меч — + 130 урона (1200 золото) 

Доступ с 6 уровня ‼️

Двермерский одноручный меч — + 155 урона (1500 золото) 

Стеклянный меч — + 185 урона ( 1850 золото) 

Двермерский двухручный меч — + 210 урона (2100 золото) 

Эльфийский  одноручный меч — + 230 урона  (2100 золото)

Меч стражи рассвета — + 270 урона ( 2550 золото ) 

Эльфийский двухручный меч — + 290 урона ( 2900 золото)

‼️‼️ Доступ с 13-го уровня ‼️‼️

Хитиновый меч — + 350 урона (  3700 золото) 

Ебанитовый меч — + 500 урона ( 5000 золото) 

Заточенный драконий меч — + 750 урона  ( 7100 золото )

Даэдрический меч — + 1000  урона  ( 10000 золото)
""", reply_markup=list_mechy)
    
# @router.message(F.text=='Уникальные оружия')
# async def shop(message: Message):
#     await message.answer("""
# Список уникальных оружий ⚔️:

# ‼️‼️ Доступ с 15-го уровня ‼️‼️

# Бритва мерунеса — + 2500 урона ( 120 рублей ) 

# Лук аурэеля — + 4700 урона ( 250 рублей ) 

# Меч мирака — + 7200 урона ( 340 рублей )

# Вутрад — + 9400 урона ( 400 рублей ) 

# Кровавая коса — + 11 700 урона ( 520 рублей ) 

# Гибель драконов — + 14 000 урона  ( 650 рублей )
# """, reply_markup=list_mechy_unic)


data_person = []

@router.message(F.text=='Пойти в путешествие 👣') #пойти в путешествие
async def treveling(message: Message):
    async with async_session() as session:
        telegram_id = message.from_user.id
        balance = random.choice(random_money)
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))

        if user.balance > 0:
            await message.answer_photo(photo='AgACAgIAAxkBAAMuZ4vA99WdY86z5hgBKUkRt7mv5gkAArjqMRsR-2BIBN7ny0QFA1YBAAMCAAN4AAM2BA', caption='Вы пошли в путешествие 🏃‍♂‍➡️')
            k, v = random.choice(list(list_random.items()))
            if k == 'Moneta':
                await asyncio.sleep(1)
                await rq.add_coins(telegram_id, balance)
                return message.answer_photo(photo=v['picture'], caption=v['description'], reply_markup=main)
            await message.answer_photo(photo=v['picture'], caption=f'{v["description"]}Урон - {v["damage"]}\nЗдоровье - {v["half"]}\nЗащита - {v["oboron"]}', reply_markup=play)
            return data_person.append(k)
        await message.answer('У вас маленький баланс! Вам нельзя идти в сражение')

@router.message(F.text=='Бежать')
async def bejat(message: Message):
    async with async_session() as session:
        telegram_id = message.from_user.id
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))

        if user.balance > 0:
            balance = random.choice(random_money)
            health = balance
            telegram_id = message.from_user.id
            await rq.take_health(telegram_id, health)
            await rq.take_coins(telegram_id, balance)
            return await message.answer(f'Вы бежали с поля боя и потеряли {balance} монет(-y)', reply_markup=main)
        await message.answer('У вас маленький маланс! Вам нельзя идти в сражение')

@router.message(F.text=='Вступить')
async def vstupit(message: Message):
    balance = random.choice(random_money)
    health = random.choice(random_health)
    telegram_id = message.from_user.id
    experience = random.choice(random_experience)
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))

        if user.balance > 0:
            for name in data_person:
                id_person = name
            if 'Ubiyca' in id_person: #если попался убийца
                for k, v in list_random.items():
                    if k == 'Ubiyca':
                        if user.damage > v["damage"]:
                            await rq.add_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            await rq.plus_experience(telegram_id, experience)
                            if user.lvl == 0 and user.experience > 35:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 1')
                            if user.lvl == 1 and user.experience > 60:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 2')
                            if user.lvl == 2 and user.experience > 80:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 3')
                            if user.lvl == 3 and user.experience > 100:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 4')
                            if user.lvl == 4 and user.experience > 135:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 5')
                            if user.lvl == 5 and user.experience > 160:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 6')
                            if user.lvl == 6 and user.experience > 195:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 7')
                            if user.lvl == 7 and user.experience > 240:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 8')
                            if user.lvl == 8 and user.experience > 290:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 9')
                            if user.lvl == 9 and user.experience > 345:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 10')
                            if user.lvl == 10 and user.experience > 380:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 11')
                            if user.lvl == 11 and user.experience > 425:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 12')
                            if user.lvl == 12 and user.experience > 480:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 13')
                            if user.lvl == 13 and user.experience > 520:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 14')
                            if user.lvl == 14 and user.experience > 600:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            if user.lvl == 15 and user.experience > 100000:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            return await message.answer(f'Поздравляю! Вы одержали победу и получили + {balance} монет(-у)\nИ + {experience} едениц опыта', reply_markup=main)
                        else:
                            await rq.take_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            return await message.answer(f'Увы! Вы проиграли. У вас забрали {balance} монет(-у)', reply_markup=main)

            if 'Bandit' in id_person: #если попался убийца
                for k, v in list_random.items():
                    if k == 'Bandit':
                        if user.damage > v["damage"]:
                            await rq.add_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            await rq.plus_experience(telegram_id, experience)
                            if user.lvl == 0 and user.experience > 35:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 1')
                            if user.lvl == 1 and user.experience > 60:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 2')
                            if user.lvl == 2 and user.experience > 80:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 3')
                            if user.lvl == 3 and user.experience > 100:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 4')
                            if user.lvl == 4 and user.experience > 135:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 5')
                            if user.lvl == 5 and user.experience > 160:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 6')
                            if user.lvl == 6 and user.experience > 195:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 7')
                            if user.lvl == 7 and user.experience > 240:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 8')
                            if user.lvl == 8 and user.experience > 290:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 9')
                            if user.lvl == 9 and user.experience > 345:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 10')
                            if user.lvl == 10 and user.experience > 380:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 11')
                            if user.lvl == 11 and user.experience > 425:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 12')
                            if user.lvl == 12 and user.experience > 480:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 13')
                            if user.lvl == 13 and user.experience > 520:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 14')
                            if user.lvl == 14 and user.experience > 600:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            if user.lvl == 15 and user.experience > 100000:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            return await message.answer(f'Поздравляю! Вы одержали победу и получили + {balance} монет(-у)\nИ + {experience} едениц опыта', reply_markup=main)
                        else:
                            await rq.take_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            return await message.answer(f'Увы! Вы проиграли. У вас забрали {balance} монет(-у)', reply_markup=main)

            if 'Vor' in id_person: #если попался убийца
                for k, v in list_random.items():
                    if k == 'Vor':
                        if user.damage > v["damage"]:
                            await rq.add_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            await rq.plus_experience(telegram_id, experience)
                            if user.lvl == 0 and user.experience > 35:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 1')
                            if user.lvl == 1 and user.experience > 60:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 2')
                            if user.lvl == 2 and user.experience > 80:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 3')
                            if user.lvl == 3 and user.experience > 100:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 4')
                            if user.lvl == 4 and user.experience > 135:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 5')
                            if user.lvl == 5 and user.experience > 160:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 6')
                            if user.lvl == 6 and user.experience > 195:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 7')
                            if user.lvl == 7 and user.experience > 240:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 8')
                            if user.lvl == 8 and user.experience > 290:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 9')
                            if user.lvl == 9 and user.experience > 345:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 10')
                            if user.lvl == 10 and user.experience > 380:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 11')
                            if user.lvl == 11 and user.experience > 425:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 12')
                            if user.lvl == 12 and user.experience > 480:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 13')
                            if user.lvl == 13 and user.experience > 520:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 14')
                            if user.lvl == 14 and user.experience > 600:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            if user.lvl == 15 and user.experience > 100000:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            return await message.answer(f'Поздравляю! Вы одержали победу и получили + {balance} монет(-у)\nИ + {experience} едениц опыта', reply_markup=main)
                        else:
                            await rq.take_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            return await message.answer(f'Увы! Вы проиграли. У вас забрали {balance} монет(-у)', reply_markup=main)

            if 'Ork' in id_person: #если попался убийца
                for k, v in list_random.items():
                    if k == 'Ork':
                        if user.damage > v["damage"]:
                            await rq.add_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            await rq.plus_experience(telegram_id, experience)
                            if user.lvl == 0 and user.experience > 35:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 1')
                            if user.lvl == 1 and user.experience > 60:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 2')
                            if user.lvl == 2 and user.experience > 80:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 3')
                            if user.lvl == 3 and user.experience > 100:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 4')
                            if user.lvl == 4 and user.experience > 135:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 5')
                            if user.lvl == 5 and user.experience > 160:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 6')
                            if user.lvl == 6 and user.experience > 195:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 7')
                            if user.lvl == 7 and user.experience > 240:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 8')
                            if user.lvl == 8 and user.experience > 290:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 9')
                            if user.lvl == 9 and user.experience > 345:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 10')
                            if user.lvl == 10 and user.experience > 380:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 11')
                            if user.lvl == 11 and user.experience > 425:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 12')
                            if user.lvl == 12 and user.experience > 480:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 13')
                            if user.lvl == 13 and user.experience > 520:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 14')
                            if user.lvl == 14 and user.experience > 600:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            if user.lvl == 15 and user.experience > 100000:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            return await message.answer(f'Поздравляю! Вы одержали победу и получили + {balance} монет(-у)\nИ + {experience} едениц опыта', reply_markup=main)
                        else:
                            await rq.take_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            return await message.answer(f'Увы! Вы проиграли. У вас забрали {balance} монет(-у)', reply_markup=main)

            if 'TemnyElf' in id_person: #если попался убийца
                for k, v in list_random.items():
                    if k == 'TemnyElf':
                        if user.damage > v["damage"]:
                            await rq.add_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            await rq.plus_experience(telegram_id, experience)
                            if user.lvl == 0 and user.experience > 35:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 1')
                            if user.lvl == 1 and user.experience > 60:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 2')
                            if user.lvl == 2 and user.experience > 80:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 3')
                            if user.lvl == 3 and user.experience > 100:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 4')
                            if user.lvl == 4 and user.experience > 135:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 5')
                            if user.lvl == 5 and user.experience > 160:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 6')
                            if user.lvl == 6 and user.experience > 195:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 7')
                            if user.lvl == 7 and user.experience > 240:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 8')
                            if user.lvl == 8 and user.experience > 290:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 9')
                            if user.lvl == 9 and user.experience > 345:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 10')
                            if user.lvl == 10 and user.experience > 380:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 11')
                            if user.lvl == 11 and user.experience > 425:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 12')
                            if user.lvl == 12 and user.experience > 480:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 13')
                            if user.lvl == 13 and user.experience > 520:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 14')
                            if user.lvl == 14 and user.experience > 600:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            if user.lvl == 15 and user.experience > 100000:
                                await rq.defoult_exp(telegram_id)
                                await rq.up_lvl(telegram_id)
                                await message.answer('Ваш уровень повысился до 15')
                            return await message.answer(f'Поздравляю! Вы одержали победу и получили + {balance} монет(-у)\nИ + {experience} едениц опыта', reply_markup=main)
                        else:
                            await rq.take_coins(telegram_id, balance)
                            await rq.take_health(telegram_id, health)
                            return await message.answer(f'Увы! Вы проиграли. У вас забрали {balance} монет(-у)', reply_markup=main)
        await message.answer('У вас маленький маланс! Вам нельзя идти в сражение')
    # await asyncio.sleep(2)
    # await message.answer(f'Вы бежали с поля боя и потеряли {balance} монет(-y)', reply_markup=main)






# @router.message(F.text=='Пойти на босса 🧝‍♂️') #пойти на боса
# async def boss(message: Message):
#     await message.answer(f'Фотка босса и описание, снизу 2 кнопки сражаться или бежать')

@router.message(F.text=='Кузница 🏠') #кузница
async def kuznica(message: Message):
    await message.answer(f'Кузница 🏠 (Магазин оружия)', reply_markup=shop_or_paupau)

# @router.message(F.text=='Бизнесы 💰') #ваши бизнесы
# async def biznes(message: Message):
#     pass
    

# @router.message(F.text=='Города 🌃') #все города
# async def all_cityes(message: Message):
#     await message.answer(f'фотка с описание и все города')

@router.message(F.text=='Фермы 🌾') #все фермы
async def ferms_all(message: Message):
    await message.answer('Фермы 🌾', reply_markup=list_my_fermies)

@router.message(F.text=='Приобрести ферму 🪵') #список всех фермы
@router.message(F.text=='Обратно к списку ферм 🔙')
async def list_by_ferms_all(message: Message):
    await message.answer(f"""
Список доступных Ферм🏡:

🐔Куринная ферма — 10 шт яйц в час
Цена: 2000 золото

🐷Свинная ферма — 15 шт мяса в час
Цена: 4500 золото

🐑Овечья ферма — 20 шерсти в час
Цена: 6000 золото

🐮Коровья ферма — 10 литра молока  в час
Цена: 8500 золото

🐎Лошадиная ферма — 20 шт лечебного молоко в час
Цена: 15500 золото
""", reply_markup=all_fermies)


@router.message(F.text=='Работы 🧑‍🌾') #все работы
@router.message(F.text=='Обратно к списку работ 🔙')
async def all_works(message: Message):
    await message.answer(f"""
Список работ:

‼️‼️Доступно с 0-го уровня ‼️‼️

👷‍♂Шахтёр — +15 золото 

‼️‼️ Доступно с 2 уровня ‼️‼️

👷‍♂Опытный шахтёр — +30 золото 
🔥Плавильщик — +50 золото
🏹Кожевник — + 75 золото

‼️‼️доступ с 4 уровня‼️‼️

🧙Зачорователь — +110 золото
⚒️Кузнец — +150 золото
💍Ювелир — + 200 золото

‼️‼️ доступ с 6 уровня ‼️‼️

🌿Алхимик — +250 золото
🥷Грабитель — +310 золото
🗡Наемный убийца — +400 золото
🐉Уничтожитель драконов — +500 золото

‼️‼️доступ с 14 уровня‼️‼️

🛡помощник ярла — +700 золото

‼️‼️Доступ с 15 уровня‼️‼️ 

🤴Ярл — +1000 золото

Чтобы уволиться, нажминте на " Уволиться с работы 🏃‍♂️"    
""", reply_markup=works_list)
    
@router.message(F.text=='Уволиться с работы 🏃‍♂️') #Уволиться с работы 
async def all_works(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        if user.work_place != '':
                await rq.clear_a_job(telegram_id)
                return await message.answer(f"""
Вы уволились с работы! Чтобы устроиться на новую работу в меню выберие кнопку "Работы 🧑‍🌾", затем выберите новую работу.

Будьте внимательны, на работу можно устроиться с определенного уровня     
""", reply_markup=main)
        return await message.answer('Вы не можете уволиться, так как у вас  нет работы!')
    
@router.message(F.text=='Сходить на работу🚶‍♂️') #Уволиться с работы 
async def go_to_work(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        now = datetime.now()
        if user.last_farm_work_time == None:
            user.last_farm_work_time = now
            await session.commit()
            await session.refresh(user)
        if user.work_place and user.last_farm_work_time and (now - user.last_farm_work_time).total_seconds() < 3600:
            return await message.answer(
                f'Вы работали недавно. Попробуйте позже!'
            )
        if user.work_place != '':
            if user.work_place == '👷‍♂Шахтёр':
                balance = 15
                await rq.add_coins(telegram_id, balance)
            if user.work_place == '👷‍♂Опытный шахтёр':
                balance = 30
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '🔥Плавильщик':
                balance = 50
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '🏹Кожевник':
                balance = 75
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '🧙Зачорователь':
                balance = 110
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '⚒️Кузнец':
                balance = 150
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '💍Ювелир':
                balance = 200
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '🌿Алхимик':
                balance = 250
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '🥷Грабитель':
                balance = 310
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '🗡Наемный убийца':
                balance = 400
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '🐉Уничтожитель драконов':
                balance = 500
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '🛡помощник ярла':
                balance = 700
                await rq.add_coins(telegram_id, balance)

            if user.work_place == '🤴Ярл':
                balance = 1000
                await rq.add_coins(telegram_id, balance)

            exl = update(User).filter(User.telegram_id == telegram_id).values(last_farm_work_time=now)
            await session.execute(exl)
            await session.commit()
            return await message.answer(f"""
Вы сходили на работу!И получили монеты!
(Важно: за каждую работу, дают определенное кол-во монет)

Чтобы устроиться на новую работу в меню выберие кнопку "Работы 🧑‍🌾", затем выберите новую работу.
Будьте внимательны, на работу можно устроиться с определенного уровня!   
""", reply_markup=main)
        return await message.answer('Вы не можете сходить на работу. У вас её нет!')
    
@router.message(F.text=='Продать меч 💰') #продать меч 
async def sell_gun(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        if user.gun != '':
            if user.gun == 'Ржавый клинок':
                balance = 80
                damage = 5
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Не заточенный железный меч':
                balance = 120
                damage = 10
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Железный меч':
                balance = 170
                damage = 20
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Стальной не заточенный меч':
                balance = 300
                damage = 30
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Имперакий меч':
                balance = 550
                damage = 50
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Стальной меч':
                balance = 750
                damage = 70
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Стальной двуручный меч':
                balance = 900
                damage = 100
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Орочьий меч':
                balance = 1150
                damage = 130
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Двермерский одноручный меч':
                balance = 1500
                damage = 155
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Стеклянный меч':
                balance = 1850
                damage = 185
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Двермерский двухручный меч':
                balance = 2100
                damage = 210
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Эльфийский одноручный меч':
                balance = 2300
                damage = 230
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Меч стражи рассвета':
                balance = 2550
                damage = 270
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Эльфийский двухручный меч':
                balance = 2900
                damage = 290
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Хитиновый меч':
                balance = 3700
                damage = 350
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Ебанитовый меч':
                balance = 5000
                damage = 500
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Заточенный драконий меч':
                balance = 7100
                damage = 750
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            if user.gun == 'Даэдрический меч':
                balance = 10000
                damage = 1000
                await rq.add_coins(telegram_id, balance)
                await rq.minus_damage(telegram_id, damage)
            await rq.clear_a_gun(telegram_id)
            return await message.answer(f"""
Вы продали свое оружие, при этом урон, который был с оружием ушел (Будьте внимательны)! Чтобы купить новое оружие в меню выберие кнопку "Оружие", затем выберите подходящую для вас категорию.

Будьте внимательны, оружие можно покупать с определенного уровня     
""", reply_markup=main)
        return await message.answer('Вы не можете продать оружие, так как его у вас нет!')
    
@router.message(F.text=='Продать броню 💰') #продать броню
async def sell_armor(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        if user.armor != '':
            if user.armor == 'Ржавая железная броня':
                balance = 400
                health = 25
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Меховая броня':
                balance = 750
                health = 50
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Кожанная броня':
                balance = 950
                health = 85
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Поношенная броня':
                balance = 1100
                health = 110
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Чешуйчатая броня':
                balance = 1850
                health = 150
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Лёгкая имперская броня':
                balance = 2100
                health = 185
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Железная броня':
                balance = 2400
                health = 215
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Офицерская броня':
                balance = 2650
                health = 260
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Хитиновая броня':
                balance = 2950
                health = 300
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Стеклянная броня':
                balance = 3400
                health = 360
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Броня из драконей чешуи':
                balance = 3750
                health = 400
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Броня стража рассвета':
                balance = 4300
                health = 500
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Броня из костей':
                balance = 7000
                health = 650
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Тяжёлая хитиновая броня':
                balance = 9500
                health = 850
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Тяжёлая броня Фалмера':
                balance = 11000
                health = 1100
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Закалённая броня Фалмера':
                balance = 14500
                health = 1250
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)
            if user.armor == 'Даэдрическая броня':
                balance = 19500
                health = 1800
                await rq.add_coins(telegram_id, balance)
                await rq.take_health(telegram_id, health)

            await rq.clear_a_armor(telegram_id)
            return await message.answer(f"""
Вы продали свою броню, при этом защита, которая был с броней ушел (Будьте внимательны)! Чтобы купить новую броню в меню выберие кнопку "Доспехи", затем выберите подходящую для вас категорию.

Будьте внимательны, броню можно покупать с определенного уровня     
""", reply_markup=main)
        return await message.answer('Вы не можете продать броню, так как её у вас нет!')
    
#Продать ферму    
@router.message(F.text=='Продать ферму 💰') #Продать ферму 
async def sell_my_buisness(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        if user.farm != '':
            if user.farm == '🐔 Куринная ферма':
                balance = 2000
                await rq.add_coins(telegram_id, balance)
            if user.farm == '🐷 Свинная ферма':
                balance = 4500
                await rq.add_coins(telegram_id, balance)
            if user.farm == '🐑 Овечья ферма':
                balance = 6000
                await rq.add_coins(telegram_id, balance)
            if user.farm == '🐮 Коровья ферма':
                balance = 10000
                await rq.add_coins(telegram_id, balance)
            if user.farm == '🐎 Лошадиная ферма':
                balance = 15500
                await rq.add_coins(telegram_id, balance)

            await rq.delete_farm(telegram_id)
            return await message.answer(f"""
Вы продали свою ферму! Чтобы купить новую, в меню выберие кнопку "Фермы 🌾", затем выберите подходящую для вас категорию.

Будьте внимательны.     
""", reply_markup=main)
        return await message.answer('Вы не можете продать ферму, так как её у вас нет!')
    

@router.message(F.text=='Моя ферма 🧑‍🌾') 
async def my_farm_check(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        if user.farm != '':
            if user.farm == '🐔 Куринная ферма':
                if user.farm_lvl == 0:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 10 яйц/час
👛 На балансе ферм: {user.farm_food} яйц🥚
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 900 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐔 Куринная ферма':
                if user.farm_lvl == 1:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 11 яйц/час
👛 На балансе ферм: {user.farm_food} яйц🥚
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 1500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐔 Куринная ферма':
                if user.farm_lvl == 2:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 15 яйц/час
👛 На балансе ферм: {user.farm_food} яйц🥚
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 2000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐔 Куринная ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 30 яйц/час
👛 На балансе ферм: {user.farm_food} яйц🥚
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)
                    

            if user.farm == '🐷 Свинная ферма':
                if user.farm_lvl == 0:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 15 кг/час
👛 На балансе ферм: {user.farm_food} кг мяса 🍖
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 1500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐷 Свинная ферма':
                if user.farm_lvl == 1:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 30 кг/час
👛 На балансе ферм: {user.farm_food} кг мяса 🍖
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 3000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐷 Свинная ферма':
                if user.farm_lvl == 2:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 38 кг/час
👛 На балансе ферм: {user.farm_food} кг мяса 🍖
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 5500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐷 Свинная ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 45 кг/час
👛 На балансе ферм: {user.farm_food} кг мяса 🍖
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)
                    

            if user.farm == '🐑 Овечья ферма':
                if user.farm_lvl == 0:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 20 шерсти/час 
👛 На балансе ферм: {user.farm_food} комков шерсти ☁️
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 1600 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐑 Овечья ферма':
                if user.farm_lvl == 1:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 40 шерсти/час 
👛 На балансе ферм: {user.farm_food} комков шерсти ☁️
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 3500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐑 Овечья ферма':
                if user.farm_lvl == 2:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 50 шерсти/час 
👛 На балансе ферм: {user.farm_food} комков шерсти ☁️
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 6000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐑 Овечья ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 60 шерсти/час 
👛 На балансе ферм: {user.farm_food} комков шерсти ☁️
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)
                    

            if user.farm == '🐮 Коровья ферма':
                if user.farm_lvl == 0:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 10 литров/час
👛 На балансе ферм: {user.farm_food} литров молока 🥛
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 2000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐮 Коровья ферма':
                if user.farm_lvl == 1:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 11 литров/час
👛 На балансе ферм: {user.farm_food} литров молока 🥛
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 4500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐮 Коровья ферма':
                if user.farm_lvl == 2:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 15 литров/час
👛 На балансе ферм: {user.farm_food} литров молока 🥛
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 7000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐮 Коровья ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 30 литров/час
👛 На балансе ферм: {user.farm_food} литров молока 🥛
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)
                    

            if user.farm == '🐎 Лошадиная ферма':
                if user.farm_lvl == 0:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 20 литров/час
👛 На балансе ферм: {user.farm_food} литров лечебного молока 🧙
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 2000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐎 Лошадиная ферма':
                if user.farm_lvl == 1:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 40 литров/час
👛 На балансе ферм: {user.farm_food} литров лечебного молока 🧙
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 4500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐎 Лошадиная ферма':
                if user.farm_lvl == 2:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 50 литров/час
👛 На балансе ферм: {user.farm_food} литров лечебного молока 🧙
✨ Уровень фермы: {user.farm_lvl}

🦾Стоимость улучшения: 7000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐎 Лошадиная ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 60 литров/час
👛 На балансе ферм: {user.farm_food} литров лечебного молока 🧙
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)


        return await message.answer('На данный момент у вас нет своей фермы!')
    

@router.message(F.text=='Собрать хозяйственные продукты')
async def my_farm_check(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        if user.farm != '':
            if user.farm == '🐔 Куринная ферма':
                if user.farm_lvl == 0 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*5)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 1 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*5)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 2 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*5)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 3 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*5)
                    return await message.answer('Продажа прошла успешно!')

                    

            if user.farm == '🐷 Свинная ферма':
                if user.farm_lvl == 0 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*20)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 1 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*20)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 2 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*20)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 3 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*20)
                    return await message.answer('Продажа прошла успешно!')



            if user.farm == '🐑 Овечья ферма':
                if user.farm_lvl == 0 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*55)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 1 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*55)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 2 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*55)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 3 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*55)
                    return await message.answer('Продажа прошла успешно!')
                    

            if user.farm == '🐮 Коровья ферма':
                if user.farm_lvl == 0 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*90)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 1 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*90)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 2 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*90)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 3 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*90)
                    return await message.answer('Продажа прошла успешно!')
                    

            if user.farm == '🐎 Лошадиная ферма':
                if user.farm_lvl == 0 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*150)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 1 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*150)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 2 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*150)
                    return await message.answer('Продажа прошла успешно!')
                if user.farm_lvl == 3 and user.farm_food != 0:
                    await rq.farm_food_update(telegram_id, food_count=user.farm_food*150)
                    return await message.answer('Продажа прошла успешно!')
                
            return await message.answer('У вас нет продуктов, которые накопились на ферме (их можно посмотреть в балансе фермы)')

        return await message.answer('Убедитесь что у вас есть ферма.')

@router.message(F.text=='Начать работу фермы 🕘')
async def start_work_farm(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))

        if user.last_farm_work_time and datetime.now() - user.last_farm_work_time < timedelta(hours=1):
            return await message.answer('Вы уже работали на ферме в последний час. Попробуйте позже.')

        if user.farm != '':
            if user.farm == '🐔 Куринная ферма':
                if user.farm_lvl == 0:
                    food_count = 10
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Курицы поработыли на славу! И принесли вам + {food_count} яиц 🥚')
                if user.farm_lvl == 1:
                    food_count = 11
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Курицы поработыли на славу! И принесли вам + {food_count} яиц 🥚')
                if user.farm_lvl == 2:
                    food_count = 15
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Курицы поработыли на славу! И принесли вам + {food_count} яиц 🥚')
                if user.farm_lvl == 3:
                    food_count = 30
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Курицы поработыли на славу! И принесли вам + {food_count} яиц 🥚')


                    
            if user.farm == '🐷 Свинная ферма':
                if user.farm_lvl == 0:
                    food_count = 15
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Свини поработыли на славу! И принесли вам + {food_count} кг мяса 🍖')
                if user.farm_lvl == 1:
                    food_count = 30
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Свини поработыли на славу! И принесли вам + {food_count} кг мяса 🍖')
                if user.farm_lvl == 2:
                    food_count = 38
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Свини поработыли на славу! И принесли вам + {food_count} кг мяса 🍖')
                if user.farm_lvl == 3:
                    food_count = 45
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Свини поработыли на славу! И принесли вам + {food_count} кг мяса 🍖')

            if user.farm == '🐑 Овечья ферма':
                if user.farm_lvl == 0:
                    food_count = 20
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Овцы поработыли на славу! И принесли вам + {food_count} комков шерсти ☁️')
                if user.farm_lvl == 1 and user.farm_food != 0:
                    food_count = 40
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Овцы поработыли на славу! И принесли вам + {food_count} комков шерсти ☁️')
                if user.farm_lvl == 2 and user.farm_food != 0:
                    food_count = 50
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Овцы поработыли на славу! И принесли вам + {food_count} комков шерсти ☁️')
                if user.farm_lvl == 3 and user.farm_food != 0:
                    food_count = 60
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Овцы поработыли на славу! И принесли вам + {food_count} комков шерсти ☁️')
                    

            if user.farm == '🐮 Коровья ферма':
                if user.farm_lvl == 0:
                    food_count = 10
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Коровы поработыли на славу! И принесли вам + {food_count} литра молока 🥛')
                if user.farm_lvl == 1:
                    food_count = 11
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Коровы поработыли на славу! И принесли вам + {food_count} литра молока 🥛')
                if user.farm_lvl == 2:
                    food_count = 15
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Коровы поработыли на славу! И принесли вам + {food_count} литра молока 🥛')
                if user.farm_lvl == 3:
                    food_count = 30
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Коровы поработыли на славу! И принесли вам + {food_count} литра молока 🥛')

                    

            if user.farm == '🐎 Лошадиная ферма':
                if user.farm_lvl == 0:
                    food_count = 20
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Лошади поработыли на славу! И принесли вам + {food_count} литра лечебного молока 🧙')
                if user.farm_lvl == 1:
                    food_count = 40
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Лошади поработыли на славу! И принесли вам + {food_count} литра лечебного молока 🧙')
                if user.farm_lvl == 2:
                    food_count = 50
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Лошади поработыли на славу! И принесли вам + {food_count} литра лечебного молока 🧙')
                if user.farm_lvl == 3:
                    food_count = 60
                    await rq.updt_food_count(telegram_id, food_count)
                    user.last_farm_work_time = datetime.now()
                    await session.commit()
                    return await message.answer(f'Лошади поработыли на славу! И принесли вам + {food_count} литра лечебного молока 🧙')

        return await message.answer('Убедитесь что у вас есть ферма.')


@router.message(F.text=='Улучшить ферму 🆙') 
async def my_farm_lvl_up(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        if user.farm != '':
            if user.farm == '🐔 Куринная ферма':
                balance = 900
                if user.farm_lvl == 0 and user.balance > 900:
                    farm_lvl = 1
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 1 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 10 яйц/час
👛 На балансе ферм: {user.farm_food} яйц🥚
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 900 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐔 Куринная ферма':
                balance = 1500
                if user.farm_lvl == 1 and user.balance > 1500:
                    farm_lvl = 2
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 2 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 11 яйц/час
👛 На балансе ферм: {user.farm_food} яйц🥚
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 1500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
            if user.farm == '🐔 Куринная ферма':
                balance = 2000
                if user.farm_lvl == 2 and user.balance > 2000:
                    farm_lvl = 3
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 3 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 15 яйц/час
👛 На балансе ферм: {user.farm_food} яйц🥚
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 2000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
                return await message.answer('У вас маленький баланс!')
            if user.farm == '🐔 Куринная ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
Поздравляем! Вы достигли максимального уровня фермы.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 30 яйц/час
👛 На балансе ферм: {user.farm_food} яйц🥚
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)


            if user.farm == '🐷 Свинная ферма':
                balance = 1500
                if user.farm_lvl == 0 and user.balance > 1500:
                    farm_lvl = 1
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 1 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 15 кг/час
👛 На балансе ферм: {user.farm_food} кг мяса 🍖
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 1500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐷 Свинная ферма':
                balance = 3000
                if user.farm_lvl == 1 and user.balance > 3000:
                    farm_lvl = 2
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 2 уровня.
                                                
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 30 кг/час
👛 На балансе ферм: {user.farm_food} кг мяса 🍖
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 3000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐷 Свинная ферма':
                balance = 5500
                if user.farm_lvl == 2 and user.balance > 5500:
                    farm_lvl = 3
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 3 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 38 кг/час
👛 На балансе ферм: {user.farm_food} кг мяса 🍖
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 5500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)
                return await message.answer('У вас маленький баланс!')
            if user.farm == '🐷 Свинная ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
Поздравляем! Вы достигли максимального уровня фермы.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 15 кг/час
👛 На балансе ферм: {user.farm_food} кг мяса 🍖
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)
                    

            if user.farm == '🐑 Овечья ферма':
                balance = 1600
                if user.farm_lvl == 0 and user.balance > 1600:
                    farm_lvl = 1
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 1 уровня.
                                                
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 20 шерсти/час 
👛 На балансе ферм: {user.farm_food} комков шерсти ☁️
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 1600 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐑 Овечья ферма':
                balance = 3500
                if user.farm_lvl == 1 and user.balance > 3500:
                    farm_lvl = 2
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 2 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 40 шерсти/час 
👛 На балансе ферм: {user.farm_food} комков шерсти ☁️
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 3500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐑 Овечья ферма':
                balance = 6000
                if user.farm_lvl == 2 and user.balance > 6000:
                    farm_lvl = 3
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 3 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 50 шерсти/час 
👛 На балансе ферм: {user.farm_food} комков шерсти ☁️
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 6000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐑 Овечья ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
Поздравляем! Вы достигли максимального уровня фермы.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 60 шерсти/час 
👛 На балансе ферм: {user.farm_food} комков шерсти ☁️
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)
                    

            if user.farm == '🐮 Коровья ферма':
                balance = 2000
                if user.farm_lvl == 0 and user.balance > 2000:
                    farm_lvl = 1
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 1 уровня.
                                                
👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 10 литров/час
👛 На балансе ферм: {user.farm_food} литров молока 🥛
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 2000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐮 Коровья ферма':
                balance = 4500
                if user.farm_lvl == 1 and user.balance > 4500:
                    farm_lvl = 2
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 2 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 11 литров/час
👛 На балансе ферм: {user.farm_food} литров молока 🥛
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 4500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐮 Коровья ферма':
                balance = 7000
                if user.farm_lvl == 2 and user.balance > 7000:
                    farm_lvl = 3
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 3 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 15 литров/час
👛 На балансе ферм: {user.farm_food} литров молока 🥛
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 7000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐮 Коровья ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
Поздравляем! Вы достигли максимального уровня фермы.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 15 литров/час
👛 На балансе ферм: {user.farm_food} литров молока 🥛
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)
                    

            if user.farm == '🐎 Лошадиная ферма':
                balance = 2000
                if user.farm_lvl == 0 and user.balance > 2000:
                    farm_lvl = 1
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 1 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 20 литров/час
👛 На балансе ферм: {user.farm_food} литров лечебного молока 🧙
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 2000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐎 Лошадиная ферма':
                balance = 4500
                if user.farm_lvl == 1 and user.balance > 4500:
                    farm_lvl = 2
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 2 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 40 литров/час
👛 На балансе ферм: {user.farm_food} литров лечебного молока 🧙
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 4500 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐎 Лошадиная фермаа':
                balance = 7000
                if user.farm_lvl == 2 and user.balance > 7000:
                    farm_lvl = 3
                    await rq.take_coins(telegram_id, balance)
                    await rq.state_lvl_farm_lvl(telegram_id, farm_lvl)
                    return await message.answer(f"""
Поздравляем! Вы улучшили свою ферму до 3 уровня.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 50 литров/час
👛 На балансе ферм: {user.farm_food} литров лечебного молока 🧙
✨ Уровень фермы: {user.farm_lvl + 1}

🦾Стоимость улучшения: 7000 золото

Что бы улучшить ферму, нажмите на кнопку "Улучшить ферму 🆙"
""", reply_markup=up_farm_lvl)

            if user.farm == '🐎 Лошадиная ферма':
                if user.farm_lvl == 3:
                    return await message.answer(f"""
Поздравляем! Вы достигли максимального уровня фермы.

👀Информация о ферме:

{user.farm}
⏳ Фермы добывают 60 литров/час
👛 На балансе ферм: {user.farm_food} литров лечебного молока 🧙
✨ Уровень фермы: {user.farm_lvl} (max)
""", reply_markup=up_farm_lvl_max)


        return await message.answer('Убедитесь что у вас есть ферма или же проверьте свой баланс в профиле!')


# shop menu
@router.message(F.text) 
async def shop_menu_heandler(message: Message):
    telegram_id = message.from_user.id
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        if user.balance > 7:
            # Это  магазин еды
            if message.text == 'Яблочный пирог':
                balance = 50
                health = 30
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Яблочный пирог')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Печёный картофель':
                balance = 7
                health = 5
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Печёный картофель')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Хлеб':
                balance = 15
                health = 10
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Хлеб')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Кусок козьего сыра':
                balance = 60
                health = 40
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Кусок козьего сыра')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Пчелиный мёд':
                balance = 40
                health = 25
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Пчелиный мёд')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Сладкий рулет':
                balance = 70
                health = 50
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Сладкий рулет')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Жареная рыба-убийца':
                balance = 120
                health = 80
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Жареная рыба-убийца')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Тушенная говядина':
                balance = 250
                health = 120
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Тушенная говядина')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Копустный суп':
                balance = 350
                health = 150
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Копустный суп')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Вареная говядина':
                balance = 500
                health = 200
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Вареная говядина')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Куригая грудка на гриле':
                balance = 670
                health = 280
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Куригая грудка на гриле')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Лошадиный окорок':
                balance = 760
                health = 340
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Лошадиный окорок')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Стейк из мамонта':
                balance = 860
                health = 420
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Стейк из мамонта')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Жаркое из фазана':
                balance = 1000
                health = 500
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Жаркое из фазана')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Отбивная из оленины':
                balance = 1350
                health = 600
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Отбивная из оленины')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Тушенная оленина':
                balance = 1550
                health = 680
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Тушенная оленина')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Стейк из лосося':
                balance = 1800
                health = 750
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Стейк из лосося')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Тушеное мясо по-Хоркерски':
                balance = 2390
                health = 920
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Тушеное мясо по-Хоркерски')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Эльсвейрское фондю':
                balance = 2750
                health = 1110
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Эльсвейрское фондю')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Ножки Грязевого краба':
                balance = 3350
                health = 1400
                if user.balance > balance:
                    await rq.take_coins(telegram_id, balance)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Ножки Грязевого краба')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
                # Это магазин орудя
            if message.text == 'Ржавый клинок':
                balance = 80
                damage = 5
                gun = 'Ржавый клинок'
                if user.balance > balance:
                    if user.lvl <= 1:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Ржавый клинок')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Не заточенный железный меч':
                balance = 120
                damage = 10
                gun = 'Не заточенный железный меч'
                if user.balance > balance:
                    if user.lvl <= 1:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Не заточенный железный меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Железный меч':
                balance = 170
                damage = 20
                gun = 'Железный меч'
                if user.balance > balance:
                    if user.lvl <= 1:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Железный меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Стальной не заточенный меч':
                balance = 300
                damage = 30
                gun = 'Стальной не заточенный меч'
                if user.balance > balance:
                    if user.lvl <= 2:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Стальной не заточенный меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Стальной меч':
                balance = 550
                damage = 50
                gun = 'Стальной меч'
                if user.balance > balance:
                    if user.lvl <= 2:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Стальной меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Стальной двуручный меч':
                balance = 800
                damage = 70
                gun = 'Стальной двуручный меч'
                if user.balance > balance:
                    if user.lvl <= 2:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Стальной двуручный меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Орочьий меч':
                balance = 1000
                damage = 125
                gun = 'Орочьий меч'
                if user.balance > balance:
                    if user.lvl <= 2:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Орочьий меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Двермерский одноручный меч':
                balance = 1500
                damage = 155
                gun = 'Двермерский одноручный меч'
                if user.balance > balance:
                    if user.lvl <= 5:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Двермерский одноручный меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Стеклянный меч':
                balance = 1850
                damage = 185
                gun = 'Стеклянный меч'
                if user.balance > balance:
                    if user.lvl <= 5:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Стеклянный меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Двермерский двухручный меч':
                balance = 2100
                damage = 230
                gun = 'Двермерский двухручный меч'
                if user.balance > balance:
                    if user.lvl <= 5:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Двермерский двухручный меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Эльфийский двухручный меч':
                balance = 2600
                damage = 265
                gun = 'Эльфийский двухручный меч'
                if user.balance > balance:
                    if user.lvl <= 5:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Эльфийский двухручный меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Меч стражи рассвета':
                balance = 2550
                gun = 'Меч стражи рассвета'
                if user.balance > balance:
                    if user.lvl <= 5:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Меч стражи рассвета')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Хитиновый меч':
                balance = 3700
                damage = 350
                gun = 'Хитиновый меч'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Хитиновый меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Ебанитовый меч':
                balance = 5000
                damage = 500
                gun = 'Ебанитовый меч'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Ебанитовый меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Заточенный драконий меч':
                balance = 7100
                damage = 750
                gun = 'Заточенный драконий меч'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Заточенный драконий меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Даэдрический меч':
                balance = 10000
                damage = 1000
                gun = 'Даэдрический меч'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данное оружие. На данный момент у вас маленький уровень!')
                    if user.gun != '':
                        return await message.answer(f'На данный момент у вас уже есть оружие - {user.gun}! Чтобы купить новое, нужно продать данное, затем нажмите на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_gun)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_gun(telegram_id, gun)
                    await rq.plus_damage(telegram_id, damage)
                    return await message.answer('Вы купили Даэдрический меч')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
                
            # #Покупка прем оружия
            # if message.text == 'Бритва мерунеса':
            #     balance = 10000000
            #     damage = 2500
            #     if user.balance > balance:
            #         await rq.take_coins(telegram_id, balance)
            #         await rq.plus_damage(telegram_id, damage)
            #         return await message.answer('Вы купили Бритва мерунеса')
            # if message.text == 'Лук аурэеля':
            #     balance = 10000000
            #     damage = 4700
            #     if user.balance > balance:
            #         await rq.take_coins(telegram_id, balance)
            #         await rq.plus_damage(telegram_id, damage)
            #         return await message.answer('Вы купили Лук аурэеля')
            # if message.text == 'Меч мирака':
            #     balance = 10000000
            #     damage = 7200
            #     if user.balance > balance:
            #         await rq.take_coins(telegram_id, balance)
            #         await rq.plus_damage(telegram_id, damage)
            #         return await message.answer('Вы купили Меч мирака')
            # if message.text == 'Вутрад':
            #     balance = 10000000
            #     damage = 9400
            #     if user.balance > balance:
            #         await rq.take_coins(telegram_id, balance)
            #         await rq.plus_damage(telegram_id, damage)
            #         return await message.answer('Вы купили Вутрад')
            # if message.text == 'Кровавая коса':
            #     balance = 10000000
            #     damage = 11700
            #     if user.balance > balance:
            #         await rq.take_coins(telegram_id, balance)
            #         await rq.plus_damage(telegram_id, damage)
            #         return await message.answer('Вы купили Кровавая коса')
            # if message.text == 'Гибель драконов':
            #     balance = 10000000
            #     damage = 14000
            #     if user.balance > balance:
            #         await rq.take_coins(telegram_id, balance)
            #         await rq.plus_damage(telegram_id, damage)
            #         return await message.answer('Вы купили Гибель драконов')


            # Покупка доспехов
            if message.text == 'Ржавая железная броня':
                balance = 400
                health = 25
                armor = 'Ржавая железная броня'
                if user.balance > balance:
                    if user.lvl <= 1:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Ржавая железная броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Меховая броня':
                balance = 750
                health = 50
                armor = 'Меховая броня'
                if user.balance > balance:
                    if user.lvl <= 1:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Меховая броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Кожанная броня':
                balance = 950
                health = 85
                armor = 'Кожанная броня'
                if user.balance > balance:
                    if user.lvl <= 1:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Кожанная броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Поношенная броня':
                balance = 1100
                health = 110
                armor = 'Поношенная броня'
                if user.balance > balance:
                    if user.lvl <= 1:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Поношенная броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Чешуйчатая броня':
                balance = 1850
                health = 150
                armor = 'Чешуйчатая броня'
                if user.balance > balance:
                    if user.lvl <= 4:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Чешуйчатая броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Лёгкая имперская броня':
                balance = 2100
                health = 185
                armor = 'Лёгкая имперская броня'
                if user.balance > balance:
                    if user.lvl <= 4:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Лёгкая имперская броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Железная броня':
                balance = 2400
                health = 215
                armor = 'Железная броня'
                if user.balance > balance:
                    if user.lvl <= 4:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Железная броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Офицерская броня':
                balance = 2650
                health = 260
                armor = 'Офицерская броня'
                if user.balance > balance:
                    if user.lvl <= 4:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Офицерская броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Хитиновая броня':
                balance = 2950
                health = 300
                armor = 'Хитиновая броня'
                if user.balance > balance:
                    if user.lvl <= 8:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Хитиновая броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Стеклянная броня':
                balance = 3400
                health = 360
                armor = 'Стеклянная броня'
                if user.balance > balance:
                    if user.lvl <= 8:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Стеклянная броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Броня из драконей чешуи':
                balance = 3750
                health = 400
                armor = 'Броня из драконей чешуи'
                if user.balance > balance:
                    if user.lvl <= 8:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Броня из драконей чешуи')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Броня стража рассвета':
                balance = 4300
                health = 500
                armor = 'Броня стража рассвета'
                if user.balance > balance:
                    if user.lvl <= 8:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Броня стража рассвета')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Броня из костей':
                balance = 7000
                health = 650
                armor = 'Броня из костей'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Броня из костей')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Тяжёлая хитиновая броня':
                balance = 8500
                health = 950
                armor = 'Тяжёлая хитиновая броня'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Тяжёлая хитиновая броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Тяжёлая броня Фалмера':
                balance = 11000
                health = 1000
                armor = 'Тяжёлая броня Фалмера'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Тяжёлая броня Фалмера')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Закалённая броня Фалмера':
                balance = 14500
                health = 1250
                armor = 'Закалённая броня Фалмера'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Закалённая броня Фалмера')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Броня из драконьих доспехов':
                balance = 17000
                health = 1450
                armor = 'Броня из драконьих доспехов'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Броня из драконьих доспехов')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
            if message.text == 'Даэдрическая броня':
                balance = 19500
                health = 1800
                armor = 'Даэдрическая броня'
                if user.balance > balance:
                    if user.lvl <= 12:
                        return await message.answer('К сожалению вам запрещено покупать данную броню. На данный момент у вас маленький уровень!')
                    if user.armor != '':
                        return await message.answer(f'На данный момент у вас уже есть броня - {user.armor}! Чтобы купить новую, нужно продать данное, нажав на кнопку "Продать" ниже в меню.', reply_markup=clear_a_list_armor)
                    await rq.take_coins(telegram_id, balance)
                    await rq.get_a_armor(telegram_id, armor)
                    await rq.plus_health(telegram_id, health)
                    return await message.answer('Вы купили Даэдрическая броня')
                return await message.answer('О нет... Ваш баланс слишком маленький.')
                

            #уникальная броня за прем
            # if message.text == 'Даэдрическая броня':
            #     balance = 19500
            #     health = 3000
            #     protection = 55
            #     if user.balance > balance:
            #         await rq.take_coins(telegram_id, balance)
            #         await rq.plus_protection(telegram_id, protection)
            #         await rq.plus_health(telegram_id, health)
            #         return await message.answer('Вы купили Даэдрическая броня')
            
 
            #Устройство на работу

            if message.text == '👷‍♂Шахтёр':
                work_place = '👷‍♂Шахтёр'
                if user.lvl <= 0:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать Шахтёром👷‍♂.')
            if message.text == '👷‍♂Опытный шахтёр':
                work_place = '👷‍♂Опытный шахтёр'
                if user.lvl <= 1:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать Шахтёром👷‍♂.')
            if message.text == '🔥Плавильщик':
                work_place = '🔥Плавильщик'
                if user.lvl <= 1:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 🔥Плавильщиком.')
            if message.text == '🏹Кожевник':
                work_place = '🏹Кожевник'
                if user.lvl <= 1:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 🏹Кожевником.')
            if message.text == '🧙Зачорователь':
                work_place = '🧙Зачорователь'
                if user.lvl <= 3:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 🧙Зачорователем.')
            if message.text == '⚒️Кузнец':
                work_place = '⚒️Кузнец'
                if user.lvl <= 3:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать ⚒️Кузнецом.')
            if message.text == '💍Ювелир':
                work_place = '💍Ювелир'
                if user.lvl <= 3:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 💍Ювелиром.')
            if message.text == '🌿Алхимик':
                work_place = '🌿Алхимик'
                if user.lvl <= 5:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 🌿Алхимиком.')
            if message.text == '🥷Грабитель':
                work_place = '🥷Грабитель'
                if user.lvl <= 5:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 🥷Грабителем.')
            if message.text == '🗡Наемный убийца':
                work_place = '🗡Наемный убийца'
                if user.lvl <= 5:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 🗡Наемным убийцей.')
            if message.text == '🐉Уничтожитель драконов':
                work_place = '🐉Уничтожитель драконов'
                if user.lvl <= 5:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 🐉Уничтожителем драконов.')
            if message.text == '🛡помощник ярла':
                work_place = '🛡помощник ярла'
                if user.lvl <= 13:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 🛡помощником ярла.')
            if message.text == '🤴Ярл':
                work_place = '🤴Ярл'
                if user.lvl <= 14:
                    return await message.answer('К сожалению вам запрещено работать. На данный момент у вас маленький уровень!')
                if user.work_place != '':
                    return await message.answer(f'На данный момент вы уже работаете {user.work_place}! Чтобы уволиться нажмите на кнопку "Уволиться" ниже в меню.', reply_markup=live_on_work_place)
                await rq.get_a_job(telegram_id, work_place)
                return await message.answer('Поздравляем! Вы устроились работать 🤴Ярлом.')
            
            #покупка бизнеса
            if message.text == '🐔 Куринная ферма':
                farm = '🐔 Куринная ферма'
                balance = 2000
                if user.farm != '':
                    return await message.answer(f'У вас уже есть ферма - {user.farm}! Чтобы купить новую, продайте старую.', reply_markup=sell_a_farm)
                if user.balance < 2000:
                    return await message.answer(f'Вы не можете купить данную ферму, у вас маленький балнс!')
                await rq.take_coins(telegram_id, balance) 
                await rq.get_a_farm(telegram_id, farm) 
                return await message.answer('Поздравляем!\nВы приобрели новую ферму - 🐔 Куринная ферма.', reply_markup=main)
            if message.text == '🐷 Свинная ферма':
                farm = '🐷 Свинная ферма'
                balance = 4500
                if user.farm != '':
                    return await message.answer(f'У вас уже есть ферма - {user.farm}! Чтобы купить новую, продайте старую.', reply_markup=sell_a_farm)
                if user.balance < 4500:
                    return await message.answer(f'Вы не можете купить данную ферму, у вас маленький балнс!')
                await rq.take_coins(telegram_id, balance) 
                await rq.get_a_farm(telegram_id, farm) 
                return await message.answer('Поздравляем!\nВы приобрели новую ферму - 🐷 Свинная ферма.', reply_markup=main)
            if message.text == '🐑 Овечья ферма':
                farm = '🐑 Овечья ферма'
                balance = 6000
                if user.farm != '':
                    return await message.answer(f'У вас уже есть ферма - {user.farm}! Чтобы купить новую, продайте старую.', reply_markup=sell_a_farm)
                if user.balance < 6000:
                    return await message.answer(f'Вы не можете купить данную ферму, у вас маленький балнс!')
                await rq.take_coins(telegram_id, balance) 
                await rq.get_a_farm(telegram_id, farm) 
                return await message.answer('Поздравляем!\nВы приобрели новую ферму - 🐑 Овечья ферма.', reply_markup=main)
            if message.text == '🐮 Коровья ферма':
                farm = '🐮 Коровья ферма'
                balance = 8500
                if user.farm != '':
                    return await message.answer(f'У вас уже есть ферма - {user.farm}! Чтобы купить новую, продайте старую.', reply_markup=sell_a_farm)
                if user.balance < 8500:
                    return await message.answer(f'Вы не можете купить данную ферму, у вас маленький балнс!')
                await rq.take_coins(telegram_id, balance) 
                await rq.get_a_farm(telegram_id, farm) 
                return await message.answer('Поздравляем!\nВы приобрели новую ферму - 🐮 Коровья ферма.', reply_markup=main)
            if message.text == '🐎 Лошадиная ферма':
                farm = '🐎 Лошадиная ферма'
                balance = 15500
                if user.farm != '':
                    return await message.answer(f'У вас уже есть ферма - {user.farm}! Чтобы купить новую, продайте старую.', reply_markup=sell_a_farm)
                if user.balance < 15500:
                    return await message.answer(f'Вы не можете купить данную ферму, у вас маленький балнс!')
                await rq.take_coins(telegram_id, balance) 
                await rq.get_a_farm(telegram_id, farm) 
                return await message.answer('Поздравляем!\nВы приобрели новую ферму - 🐎 Лошадиная ферма.', reply_markup=main)
            
        
        return await message.answer('У вас маленький баланс или уровень!')





# настройки

@router.message(F.photo)
async def photo(message: Message):
    res = message.photo[-1].file_id
    await message.answer(res)