
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# Обычные кнопки

button_hi = KeyboardButton('Привет! 👋')
button_start = KeyboardButton('Начать 🟢')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, 
one_time_keyboard=True).add(button_hi).add(button_start)



button_bone = ReplyKeyboardMarkup(resize_keyboard=True, 
one_time_keyboard=True).add(
KeyboardButton('🎲',
callback_data='your_turn')
)

coast_pyrpose = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Проезд 🚖'),
    KeyboardButton('Продукты 🍗'),
    KeyboardButton('Медицина 🚑'),
    KeyboardButton('Связь ☎️'),
    KeyboardButton('Развлечения 🏂'),
    KeyboardButton('Другое 📦'),
)


# Инлайновая клавиатура

start_kb = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton('Начать! 🟢', callback_data='start_bt'),
)

rate = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("Назад 🔙", callback_data='start_bt')
    )


main_kb = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("Игры 🎮", callback_data='game'),
    InlineKeyboardButton("Расходы 💵", callback_data='costs'),
    InlineKeyboardButton("Курсы валют 📈", callback_data='rate'),
    # InlineKeyboardButton("Назад 🔙", callback_data='####')
    )

create_db = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("Создать БД 🗄", callback_data='create_new_db'),
    InlineKeyboardButton("Назад 🔙", callback_data='start_bt')
    )


new_costs = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("Новый расход ✏️", callback_data='new_costs'),
    InlineKeyboardButton("За сегодня", callback_data='today_cost'),
    InlineKeyboardButton("За вчера", callback_data='yesterday_cost'),
    InlineKeyboardButton("За всё время", callback_data='all_cost'),
    # InlineKeyboardButton("Последние 5", callback_data='last_5_cost'),
    # InlineKeyboardButton("За неделю", callback_data='week_cost'),
    # InlineKeyboardButton("За месяц", callback_data='month_cost'),
    # InlineKeyboardButton("За год", callback_data='year_cost'),
    InlineKeyboardButton("Назад 🔙", callback_data='start_bt')
    )

# coast_categories = InlineKeyboardMarkup(row_width=2).add(
#     InlineKeyboardButton("Проезд 🚖", callback_data='taxi'),
#     InlineKeyboardButton("Продукты 🍗", callback_data='eat'),
#     InlineKeyboardButton("Медицина 🚑", callback_data='med'),
#     InlineKeyboardButton("Связь ☎️", callback_data='call'),
#     InlineKeyboardButton("Развлечения 🏂", callback_data='fan'),
#     )


# settings_buttons = InlineKeyboardMarkup(row_width=1).insert(
# InlineKeyboardButton(text="Купить премиум", callback_data="buy_premium")
# )


game_kb = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("Кости 🎲", callback_data='bones_game'),
    InlineKeyboardButton("Кости на очки 🎲", callback_data='bones_game_money'),
    InlineKeyboardButton("Слоты 🎰", callback_data='bandit_game'),
    InlineKeyboardButton("Мой счёт 💰", callback_data='check_money'),
    InlineKeyboardButton("Назад 🔙", callback_data='start_bt')
    # Добавить ёще игры
    )

game_bones_start = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Играть", callback_data='bones_game_start'),
    InlineKeyboardButton("Назад 🔙", callback_data='game')
    )

thr_die_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Бросить кубик 🎲", callback_data='thr_die')
    )

game_bones_money_start = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Играть", callback_data='bones_game_money_start'),
    InlineKeyboardButton("Назад 🔙", callback_data='game')
    )

thr_die_money_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Бросить кубик 🎲", callback_data='thr_die_money')
    )

thr_die_again_money_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Бросить ещё 🎲", callback_data='bones_game_money_start'),
    InlineKeyboardButton("Выход ↩️", callback_data='game')
    )





thr_die_again_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Бросить ещё 🎲", callback_data='thr_die'),
    InlineKeyboardButton("Выход ↩️", callback_data='game')
    )

spin_money_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Крутить 🎰", callback_data='spin_start'),
    )

spin_money_again_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Крутить ещё 🎰", callback_data='bandit_game'),
    InlineKeyboardButton("Выход ↩️", callback_data='game'),
    )

back_game = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Назад ↩️", callback_data='game'),
    )


