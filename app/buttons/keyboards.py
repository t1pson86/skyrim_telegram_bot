from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Профиль 🧙‍♂️'), KeyboardButton(text='Таверна 🛖'), KeyboardButton(text='Пойти в путешествие 👣')],
        [ KeyboardButton(text='Кузница 🏠'), KeyboardButton(text='Фермы 🌾'), KeyboardButton(text='Работы 🧑‍🌾')],
        [KeyboardButton(text='Сходить на работу🚶‍♂️')],
        [KeyboardButton(text='Уровни 💫')]
        ],
        resize_keyboard=True
)

works_list = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='👷‍♂Шахтёр'),KeyboardButton(text='👷‍♂Опытный шахтёр'), KeyboardButton(text='🔥Плавильщик'), KeyboardButton(text='🏹Кожевник')],
        [KeyboardButton(text='🧙Зачорователь'), KeyboardButton(text='⚒️Кузнец'), KeyboardButton(text='💍Ювелир')],
        [KeyboardButton(text='🌿Алхимик'), KeyboardButton(text='🥷Грабитель'), KeyboardButton(text='🗡Наемный убийца')],
        [KeyboardButton(text='🐉Уничтожитель драконов'), KeyboardButton(text='🛡помощник ярла')],
        [KeyboardButton(text='🤴Ярл')],
        [KeyboardButton(text='Уволиться с работы 🏃‍♂️')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

eat_shop = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Яблочный пирог'), KeyboardButton(text='Печёный картофель'), KeyboardButton(text='Хлеб')],
        [KeyboardButton(text='Кусок козьего сыра'), KeyboardButton(text='Сладкий рулет'), KeyboardButton(text='Жареная рыба-убийца')],
        [KeyboardButton(text='Пчелиный мёд'), KeyboardButton(text='Тушенная говядина'), KeyboardButton(text='Копустный суп')],
        [KeyboardButton(text='Вареная говядина'), KeyboardButton(text='Куриная грудка на гриле'), KeyboardButton(text='Лошадиный окорок')],
        [KeyboardButton(text='Стейк из мамонта'), KeyboardButton(text='Жаркое из фазана'), KeyboardButton(text='Отбивная из оленины')],
        [KeyboardButton(text='Тушенная оленина'), KeyboardButton(text='Стейк из лосося'), KeyboardButton(text='Тушеное мясо по-Хоркерски')],
        [KeyboardButton(text='Эльсвейрское фондю'), KeyboardButton(text='Ножки Грязевого краба')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

play = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Вступить'), KeyboardButton(text='Бежать')],
        ],
        resize_keyboard=True
)

live_on_work_place = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Уволиться с работы 🏃‍♂️')],
        [KeyboardButton(text='Обратно к списку работ 🔙')],
        ],
        resize_keyboard=True
)

clear_a_list_gun = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Продать меч 💰')],
        [KeyboardButton(text='Обратно к списку орудий 🔙')],
        ],
        resize_keyboard=True
)

clear_a_list_armor = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Продать броню 💰')],
        [KeyboardButton(text='Обратно к списку доспехов 🔙')],
        ],
        resize_keyboard=True
)

sell_a_farm = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Продать ферму 💰')],
        [KeyboardButton(text='Обратно к списку ферм 🔙')],
        ],
        resize_keyboard=True
)

up_farm_lvl = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Улучшить ферму 🆙'), KeyboardButton(text='Продать ферму 💰')],
        [KeyboardButton(text='Начать работу фермы 🕘'), KeyboardButton(text='Собрать хозяйственные продукты')],
        [KeyboardButton(text='Обратно к списку ферм 🔙')],
        ],
        resize_keyboard=True
)

up_farm_lvl_max = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Продать ферму 💰'), KeyboardButton(text='Собрать хозяйственные продукты')],
        [KeyboardButton(text='Начать работу фермы 🕘')],
        [KeyboardButton(text='Обратно к списку ферм 🔙')],
        ],
        resize_keyboard=True
)

shop_or_eat = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Еда')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

go_to_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

shop_or_paupau = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Оружие'), KeyboardButton(text='Доспехи')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

mechy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Мечи')],
        [KeyboardButton(text='Продать меч 💰')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True)

dospehy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Броня'), KeyboardButton(text='Тяжёлая броня')],
        [KeyboardButton(text='Продать броню 💰')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

list_mechy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ржавый клинок'), KeyboardButton(text='Не заточенный железный меч')],
        [KeyboardButton(text='Железный меч'), KeyboardButton(text='Стальной не заточенный меч')],
        [KeyboardButton(text='Стальной меч'), KeyboardButton(text='Стальной двуручный меч')],
        [KeyboardButton(text='Орочьий меч'), KeyboardButton(text='Двермерский одноручный меч')],
        [KeyboardButton(text='Двермерский двухручный меч'), KeyboardButton(text='Эльфийский  одноручный меч')],
        [KeyboardButton(text='Меч стражи рассвета'), KeyboardButton(text='Эльфийский двухручный меч')],
        [KeyboardButton(text='Хитиновый меч'), KeyboardButton(text='Ебанитовый меч')],
        [KeyboardButton(text='Заточенный драконий меч'), KeyboardButton(text='Даэдрический меч')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

list_mechy_unic = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Бритва мерунеса'), KeyboardButton(text='Лук аурэеля')],
        [KeyboardButton(text='Меч мирака'), KeyboardButton(text='Вутрад')],
        [KeyboardButton(text='Кровавая коса'), KeyboardButton(text='Гибель драконов')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

list_bronya = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ржавая железная броня'), KeyboardButton(text='Меховая броня')],
        [KeyboardButton(text='Кожанная броня'), KeyboardButton(text='Поношенная броня')],
        [KeyboardButton(text='Чешуйчатая броня'), KeyboardButton(text='Лёгкая имперская броня')],
        [KeyboardButton(text='Железная броня'), KeyboardButton(text='Офицерская броня')],
        [KeyboardButton(text='Хитиновая броня'), KeyboardButton(text='Стеклянная броня')],
        [KeyboardButton(text='Броня из драконей чешуи'), KeyboardButton(text='Броня стража рассвета')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

list_bronya_tyajelaya = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Броня из костей'), KeyboardButton(text='Тяжёлая хитиновая броня')],
        [KeyboardButton(text='Тяжёлая броня Фалмера'), KeyboardButton(text='Закалённая броня Фалмера')],
        [KeyboardButton(text='Броня из драконьих доспехов'), KeyboardButton(text='Даэдрическая броня')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

list_bronya_unic = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Древние доспехи Фалмеров'), KeyboardButton(text='Древние закутанные доспехи')],
        [KeyboardButton(text='Доспехи Старых богов'), KeyboardButton(text='Доспехи Ахзидала')],
        [KeyboardButton(text='Набор доспехов гильдмастера'), KeyboardButton(text='Доспехи Смертоносца')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

all_fermies = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🐔 Куринная ферма'), KeyboardButton(text='🐷 Свинная ферма')],
        [KeyboardButton(text='🐮 Коровья ферма'), KeyboardButton(text='🐑 Овечья ферма')],
        [KeyboardButton(text='🐎 Лошадиная ферма')],
        [KeyboardButton(text='Моя ферма 🧑‍🌾'), KeyboardButton(text='Продать ферму 💰')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)

list_my_fermies = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Приобрести ферму 🪵'), KeyboardButton(text='Моя ферма 🧑‍🌾')],
        [KeyboardButton(text='Главное меню 🔙')]
        ],
        resize_keyboard=True
)