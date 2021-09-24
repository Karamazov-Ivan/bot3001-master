
import asyncio
import logging
import config
import random
import kb_key
import usd_rub

from typing import Union
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from aiogram.utils.exceptions import BotBlocked
from sqler import SQLighter, SQL_file_record
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import MemoryStorage #1
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import Command
from info import Test, Game, Slot
from aiogram.dispatcher import FSMContext

# Объект бота
bot = Bot(token=config.TOKEN)

# Диспетчер для бота 
"""1#На первой строчке мы указали хранилище состояний в оперативной памяти,
так как потеря этих состояний нам не страшна (да и этот вариант больше всего подходит для демонстрационны`х целей,
так как не требует настройки). Однако если у вас от состояний что-то зависит, рекомендуется ипользовать более надеждное хранилище.
На данный момент можно подключить Redis и RethinkDB.

#2 На второй строчке подключаем логгирование.
На нем долго останавливаться не буду - лучше проверьте его работу самостоятельно: например,
можно добавить хэндлер только на текстовые сообщения, тогда при отправке стикера, фото (и т.п.), поста в канал,
где бот является администратором, в логах увидите, что эти апдейты не отработаны никаким хэндлером."""

dp = Dispatcher(bot, storage=MemoryStorage()) #1
dp.middleware.setup(LoggingMiddleware()) #2

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Инициализируем соединение с БД
db = SQLighter('baza.db')
file_db = SQL_file_record('baza.db')



#________________________________________

       
# Стартовый хэндлер\кнопка
@dp.message_handler(commands="start")
async def start(message: types.Message):
    me = await bot.get_me()
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIBbWEBY0qJDXOtzVbO_Z76g3645-OlAAIFAAPANk8T-WpfmoJrTXUgBA")
    await message.answer(f"""Добро пожаловать, {message.from_user.first_name}!\nЯ - <b>{me.first_name}</b>, бот для контроля расходов.
Напиши /help в чат, если будет нужна помощь.
Для вызова меню напиши /menu.
Желаю приятной работы""", parse_mode='html')   

    
    if len(db.check_user(message.from_user.id)) > 0:    
        print(f"Пользователь {message.from_user.id} уже в БД")

        await message.answer("Как хорошо, что ты снова здесь ☺️")

    else:
        db.add_user(message.from_user.id, message.from_user.first_name)
        print(f"Данные {message.from_user.id}, Пользователя {message.from_user.first_name} добавлены в БД")

        # Имитатор загрузки
        a = await message.answer("Ваши данные сохраняются.")
        await asyncio.sleep(0.5)   
        for i in range(3):
            b = await bot.edit_message_text("Ваши данные сохраняются..", chat_id=message.from_user.id, message_id=(a['message_id']))
            await asyncio.sleep(0.5)
            c = await bot.edit_message_text("Ваши данные сохраняются...", chat_id=message.from_user.id, message_id=(b['message_id']))
            await asyncio.sleep(0.5)
            await bot.edit_message_text("Ваши данные сохраняются....", chat_id=message.from_user.id, message_id=(c['message_id']))
            await asyncio.sleep(0.5)
            await bot.edit_message_text("Ваши данные сохраняются.", chat_id=message.from_user.id, message_id=(a['message_id']))
            await asyncio.sleep(0.5)
        await bot.edit_message_text("Готово. Вся необходимая информация у нас. Благодарим за сотрудничество. Всего доброго 😛",
        chat_id=message.from_user.id, message_id=(a['message_id']))

# Стартовые кнопки
# Кнопка с надписью "Начать!"
@dp.message_handler(commands="menu")
async def start(message: types.Message):
    
        # Проверяем есть ли пользователь в базе, на тот случай, если он пропустил /start
    if len(db.check_user(message.from_user.id)) > 0:    
        print(f"Пользователь {message.from_user.id} уже в БД")
    else:
        db.add_user(message.from_user.id, message.from_user.first_name)
        print(f"Данные {message.from_user.id}, Пользователя {message.from_user.first_name} добавлены в БД")

    await bot.send_message(message.chat.id, text="Приступим?", reply_markup=kb_key.start_kb)

# Кнопка с надписью "Игры\финансы"
@dp.callback_query_handler(text="start_bt")
async def send_random_value(call: types.CallbackQuery):
    await call.answer()
    # await call.message.answer(text='Что будем делать?', reply_markup=kb_key.main_kb)
    # await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.edit_message_text(text = "<b>Что будем делать?</b>",
    reply_markup=kb_key.main_kb,
    chat_id=call.from_user.id,
    message_id=call.message.message_id,
    parse_mode='html'
    )

# Кнопки с играми
@dp.callback_query_handler(text="game")
async def gamekey(call: types.CallbackQuery):
    await bot.edit_message_text(text="Не густо конечно...",
    reply_markup=kb_key.game_kb, chat_id=call.from_user.id,
    message_id=call.message.message_id,
    parse_mode='html'
    )

# Bones
@dp.callback_query_handler(text="bones_game")
async def gamebone(call: types.CallbackQuery):
    await bot.edit_message_text(text="Правила такие: у кого больше выпадет на кубике, тот и победил. Всё просто!\nНу,что скажешь? 🧐",
    reply_markup=kb_key.game_bones_start,
    chat_id=call.from_user.id,
    message_id=call.message.message_id
    )
    
@dp.callback_query_handler(text="bones_game_start")
async def start_gaming(call: types.CallbackQuery):
    await bot.edit_message_text(text="Нажми чтобы бросить",
    reply_markup=kb_key.thr_die_kb,
    chat_id=call.from_user.id,
    message_id=call.message.message_id
    )

# Переменные с фразами для игры "Кости"
victory = ("Получается, я победил 😼", "Сегодня не твой день", "Может быть в другой раз",
    "Не расстраивайся.. Хотя нет, расстраивайся 😈", "Приходи в другой раз, может тогда тебе повезёт больше",
    "Моя взяла", "Хе-хе-хе, я победил!!!")
lose = ("Сегодня точно не мой день 😿", "Так не пойдет, дай мне отыграться",
"Давай ещё разочек", "Удача мнё ущё улыбнётся", "Дружочек, давай ещё разочек 😉",
"Я сдаюсь... 😭\nХотя знаешь что, давай ещё!")

# Игра кости
@dp.callback_query_handler(text="thr_die")
async def start_gaming1(call: types.CallbackQuery):
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id,message_id=call.message.message_id) # Удалить сообщение
    user_die = await bot.send_dice(chat_id=call.from_user.id)
    print(f"Очков на кубике {user_die['dice']['value']}")
    await asyncio.sleep(4)
    await bot.send_message(text=f"У тебя выпало {user_die['dice']['value']}",chat_id=call.from_user.id)
    await asyncio.sleep(2)
    await bot.send_message(text="Теперь моя очередь",chat_id=call.from_user.id)
    await asyncio.sleep(2)
    bot_die = await bot.send_dice(chat_id=call.from_user.id)
    await asyncio.sleep(4)
    print(f"Очков на кубике {bot_die['dice']['value']}")
    await bot.send_message(text=f"У меня {bot_die['dice']['value']}",chat_id=call.from_user.id)
    await asyncio.sleep(1)
    if ( bot_die['dice']['value'] ) > ( user_die['dice']['value'] ):
        # Выбираем рандомную фразу из victory
        await bot.send_message(text=victory[random.randint(0, (len(victory)-1))], chat_id=call.from_user.id)
    elif ( bot_die['dice']['value'] ) < ( user_die['dice']['value'] ):
        # Выбираем рандомную фразу из lose
        await bot.send_message(text=lose[random.randint(0, (len(lose)-1))], chat_id=call.from_user.id)
    else: await bot.send_message(text="Ничья 🤔", chat_id=call.from_user.id)
    await asyncio.sleep(1)
    await bot.send_message(text="Играем ещё?", reply_markup=kb_key.thr_die_again_kb, chat_id=call.from_user.id)

# Проверить игровой счёт
@dp.callback_query_handler(text="check_money")
async def start_gaming1_money(call: types.CallbackQuery):
    await call.answer()
    await bot.edit_message_text(text=f"Денег на счёте <b>{round(db.check_money(call.from_user.id)[0][0], 2)} ₽</b>",
    reply_markup=kb_key.back_game,
    chat_id=call.from_user.id,
    message_id=call.message.message_id,
    parse_mode='html'
    )


# Кости на очки
@dp.callback_query_handler(text="bones_game_money")
async def gamebone_money(call: types.CallbackQuery):
    await bot.edit_message_text(text="Делай ставку и играй. Правила такие: у кого больше выпадет на кубике, тот и победил. Выигравший забирает банк. Всё просто!\nНу,что скажешь? 🧐",
    reply_markup=kb_key.game_bones_money_start,
    chat_id=call.from_user.id,
    message_id=call.message.message_id
    )


@dp.callback_query_handler(text="bones_game_money_start",state=None)
async def new_game_money(message:types.Message):
    await message.answer()
    if db.check_money(message.from_user.id)[0][0] ==  0:
        await bot.edit_message_text(text="Сначала пополни счёт!\nУ тебя: <b>0</b>",
            reply_markup=kb_key.game_bones_money_start,
            chat_id=message.from_user.id,
            message_id=message.message.message_id,
            parse_mode='html'
            )

    elif len(db.check_money(message.from_user.id)) > 0:
        await bot.send_message(text=f"Делай ставку\nУ тебя на счёте: {db.check_money(message.from_user.id)[0][0]}", chat_id=message.from_user.id,)
        await Game.g1.set()

@dp.message_handler(state=Game.g1)
async def answer_g1_money(message: types.Message, state:FSMContext):

    bet = message.text

    if not (bet.isdigit()):
        await bot.send_message(text="Допускается только целое число! 😡", chat_id=message.from_user.id,)
        await Game.g1.set()

    else:  
        if int(bet) > db.check_money(message.from_user.id)[0][0]:
            await bot.send_message(text="У тебя столько нет! 😡", chat_id=message.from_user.id,)
            await Game.g1.set()
            
        else:

            await state.update_data(answer1=bet)

            # Достаём переменные
            data = await state.get_data()

            global data_bet
        
            data_bet = data['answer1'] # Величина ставки
            
            await message.answer("Ставка Сделана!\nБросить кубик?", reply_markup=kb_key.thr_die_money_kb)
            
            await state.finish()
        
        


@dp.callback_query_handler(text="bones_game_money_start")
async def start_gaming_money(call: types.CallbackQuery):
    await bot.edit_message_text(text="Нажми чтобы бросить",
    reply_markup=kb_key.thr_die_money_kb,
    chat_id=call.from_user.id,
    message_id=call.message.message_id
    )

@dp.callback_query_handler(text="thr_die_money")
async def start_gaming1_money(call: types.CallbackQuery):
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id,message_id=call.message.message_id) # Удалить сообщение
    user_die = await bot.send_dice(chat_id=call.from_user.id)
    print(f"Очков на кубике {user_die['dice']['value']}")
    await asyncio.sleep(4.5)
    await bot.send_message(text=f"У тебя выпало {user_die['dice']['value']}",chat_id=call.from_user.id)
    await asyncio.sleep(2)
    await bot.send_message(text="Теперь моя очередь",chat_id=call.from_user.id)
    await asyncio.sleep(2)
    bot_die = await bot.send_dice(chat_id=call.from_user.id)
    await asyncio.sleep(4.5)
    print(f"Очков на кубике {bot_die['dice']['value']}")
    await bot.send_message(text=f"У меня {bot_die['dice']['value']}",chat_id=call.from_user.id)
    await asyncio.sleep(1)
    
    bet = int(data_bet)


    if ( bot_die['dice']['value'] ) > ( user_die['dice']['value'] ):

        db.update_money(call.from_user.id, money=( bet * (-1)) ) # data_bet - global переменная из answer_g1_money()
        # Выбираем рандомную фразу из victory

        await bot.send_message(text=f"{victory[random.randint(0, (len(victory)-1))]}\nТы проиграл: {bet}\nОстаток: {db.check_money(call.from_user.id)[0][0]}", chat_id=call.from_user.id)


    elif ( bot_die['dice']['value'] ) < ( user_die['dice']['value'] ):
        # Выбираем рандомную фразу из lose
        db.update_money(call.from_user.id, money=( bet) ) # data_bet - global переменная из answer_g1_money()
        await bot.send_message(text=f"{lose[random.randint(0, (len(lose)-1))]}\nТы выиграл: {bet * 2}\nОстаток: {db.check_money(call.from_user.id)[0][0]}", chat_id=call.from_user.id)

    else: await bot.send_message(text="Ничья 🤔", chat_id=call.from_user.id)
    await asyncio.sleep(1)
    await bot.send_message(text="Играем ещё?", reply_markup=kb_key.thr_die_again_money_kb, chat_id=call.from_user.id)




# # Игра "однорукий бандит"


@dp.callback_query_handler(text="bandit_game",state=None)
async def new_game_money(message:types.Message):
    await message.answer()
    if db.check_money(message.from_user.id)[0][0] ==  0:
        await bot.edit_message_text(text="Сначала пополни счёт!\nУ тебя: <b>0</b> ₽",
            reply_markup=kb_key.game_bones_money_start,
            chat_id=message.from_user.id,
            message_id=message.message.message_id,
            parse_mode='html'
            )

    elif len(db.check_money(message.from_user.id)) > 0:
        await bot.send_message(text=f"Делай ставку\nУ тебя на счёте: {round(db.check_money(message.from_user.id)[0][0], 2)} ₽", chat_id=message.from_user.id,)
        await Slot.s1.set()



@dp.message_handler(state=Slot.s1)
async def answer_g1_money(message: types.Message, state:FSMContext):
    slot_bet = message.text
    if not (slot_bet.isdigit()):
        await bot.send_message(text="Допускается только целое число! 😡", chat_id=message.from_user.id,)
        await Slot.s1.set()
    else:  
        if int(slot_bet) > db.check_money(message.from_user.id)[0][0]:
            await bot.send_message(text="У тебя столько нет! 😡", chat_id=message.from_user.id,)
            await Slot.s1.set()            
        else:
            await state.update_data(answer1=slot_bet)
            # Достаём переменные
            data = await state.get_data()
            global data_slot_bet
            data_slot_bet = data['answer1'] # Величина ставки
            await message.answer("Ставка Сделана!\nИграем!", reply_markup=kb_key.spin_money_kb)          
            await state.finish()
        
        


@dp.callback_query_handler(text="spin_start")
async def start_gaming1_money(call: types.CallbackQuery):
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id,message_id=call.message.message_id) # Удалить сообщение
    db.update_money(call.from_user.id, money=int(data_slot_bet) * -1) # data_bet - global переменная из answer_g1_money()
    # dice  = await bot.send_dice(emoji="🎰", chat_id=call.from_user.id)

    slot_bet = int(data_slot_bet)
    freeze_bet = slot_bet / 5
    slot_list = []

    for i in range(5):
        

        dice = await bot.send_dice(emoji="🎰", chat_id=call.from_user.id)
        await asyncio.sleep(2)
        count = await bot.send_message(text=f'В игре: {int(slot_bet)} ₽', chat_id=call.from_user.id)
        print(f"Очков на автомате {dice['dice']['value']}")
        if (dice['dice']['value']) == 64:
            slot_bet *= 10
            await bot.send_sticker(call.from_user.id, "CAACAgIAAxUAAWERQlfTRSiy9OSsxm3j6WUxp5ifAAIDAQACVp29CgLl0XiH5fpPIAQ")
            await asyncio.sleep(4)
            if (dice['dice']['value']) in slot_list:
                slot_bet *= 100
                await bot.send_sticker(call.from_user.id, "CAACAgIAAxUAAWERQlfTRSiy9OSsxm3j6WUxp5ifAAIDAQACVp29CgLl0XiH5fpPIAQ")
                await asyncio.sleep(5)
        elif (dice['dice']['value']) == 1:
            slot_bet *= 4
            await bot.send_sticker(call.from_user.id, "CAACAgIAAxkBAAITi2ERSv-TKroix7uIPxpfbBgrYYE5AAIEAQAC9wLIDyAPdzvpq8hJIAQ")
            if (dice['dice']['value']) in slot_list:
                slot_bet *= 10
        elif (dice['dice']['value']) == 22:
            if (dice['dice']['value']) in slot_list:
                slot_bet *= 5
            slot_bet *= 3
        elif (dice['dice']['value']) == 43:
            slot_bet *= 2
        else:
            slot_bet -= freeze_bet

        slot_list.append(dice['dice']['value'])
        await asyncio.sleep(4)


    await bot.send_message(text=f"В итоге {int(slot_bet)} ₽", chat_id=call.from_user.id, reply_markup=kb_key.spin_money_again_kb)
    db.update_money(call.from_user.id, money=slot_bet) # data_bet - global переменная из answer_g1_money()
    print(f"Юзер выиграл: {slot_bet}")
    
    


# Курс валют
@dp.callback_query_handler(text="rate")
async def costs_start(call: types.CallbackQuery):
    await call.answer()

    loading1 = await bot.send_message(text="Загружаю...", chat_id=call.from_user.id)

    await bot.edit_message_text(text=f"Курс доллара 🇺🇸: {usd_rub.usd()}\nКурс евро 🇪🇺: {usd_rub.eur()}\nКурс тенге 🇰🇿: {usd_rub.tng()}",
    chat_id=call.from_user.id,
    reply_markup=kb_key.rate,
    message_id=call.message.message_id
    )
    
    await bot.delete_message(chat_id=call.from_user.id, message_id=loading1['message_id'])


################################################

# async def foo():
#     print('Running in foo')
#     await asyncio.sleep(0)
#     print('Explicit context switch to foo again')


# async def bar():
#     print('Explicit context to bar')
#     await asyncio.sleep(0)
#     print('Implicit context switch back to bar')


# ioloop = asyncio.get_event_loop()
# tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
# wait_tasks = asyncio.wait(tasks)
# ioloop.run_until_complete(wait_tasks)
# ioloop.close()


################################################



@dp.callback_query_handler(text="costs")
async def costs_start(call: types.CallbackQuery):
    await call.answer()
    if len(db.check_user_status(call.from_user.id)) == 0:
        await bot.edit_message_text(text=f"Приступим. Для начала предлагаю создать БД для контроля расходов",
            chat_id=call.from_user.id,
            reply_markup=kb_key.create_db,
            message_id=call.message.message_id
            )
    else:
        await bot.edit_message_text(text=f"Можешь записать расходы или сделать выгрузку",
        chat_id=call.from_user.id,
        reply_markup=kb_key.new_costs,
        message_id=call.message.message_id
        )

# Создание БД для юзера
@dp.callback_query_handler(text="create_new_db")
async def create_db(call: types.CallbackQuery):

    await call.answer()

    if len(db.check_user_status(call.from_user.id)) == 0:

        db.cost_create_table(call.from_user.id)
        print(f"Создана база данных {call.from_user.id} для пользователя {call.from_user.first_name}")
        db.update_user_status(call.from_user.id, True)
        print(f"Для юзера {call.from_user.id} {call.from_user.first_name}, значение status = True")
        a = await bot.send_message(text="Создаём БД.",chat_id=call.from_user.id)
        await asyncio.sleep(0.5)   
        for i in range(3):
            b = await bot.edit_message_text("Создаём БД..", chat_id=call.from_user.id, message_id=(a['message_id']))
            await asyncio.sleep(0.5)
            c = await bot.edit_message_text("Создаём БД...", chat_id=call.from_user.id, message_id=(b['message_id']))
            await asyncio.sleep(0.5)
            await bot.edit_message_text("Создаём БД....", chat_id=call.from_user.id, message_id=(c['message_id']))
            await asyncio.sleep(0.5)
            await bot.edit_message_text("Создаём БД.", chat_id=call.from_user.id, message_id=(a['message_id']))
            await asyncio.sleep(0.5)
        await bot.delete_message(message_id=(a['message_id']),chat_id=call.from_user.id)
        await bot.edit_message_text("Готово. Новая база данных в твоём распоряжении",
        chat_id=call.from_user.id, message_id=call.message.message_id,reply_markup=kb_key.new_costs)
    else:
        print(f"БД {call.from_user.id} для пользователя {call.from_user.first_name} уже существует")
        await bot.send_message(text="Вы уже создали БД", chat_id=call.from_user.id, reply_markup=kb_key.new_costs)
        print(call.message.message_id)


##################################################################
#                        
#                            TEST

#_________________________________________________________________


@dp.callback_query_handler(text="new_costs",state=None)
async def create_new_cost(message:types.Message):
    await message.answer()
    await bot.send_message(text="Сколько ты протратил?\nПример:\n100500", chat_id=message.from_user.id,)
    
    #Variant 1
    await Test.q1.set()

    #Variant 2
    #await Test.first()
    #.next() or .last()

@dp.message_handler(state=Test.q1)
async def answer_q1(message: types.Message, state:FSMContext):



    # Variant 1
    cost_value_q1 = message.text

    if not (cost_value_q1.isdigit()):
        await bot.send_message(text="Допускается только целое число! 😡", chat_id=message.from_user.id,)
        await Test.q1.set()

    else:  
   
        # Variant 2
        # state = dp.current_state(chat=message.chat.id, users=messagae.from_user.id)


        # Variant 1
        await state.update_data(answer1=cost_value_q1)

        # Variant 2

        # await state.update_data(
        #     {"answer1": answer}
        #     )

        #Variant 3
        # async with state.proxy() as data:
        #     data["answer1"] = answer


        #Это:
        # async with state.proxy() as data:
        #     data["some_list"].append(1)
        # Равно этому:
        # data = await state.get_data()
        # some_list = data.get("some_list")
        # some_list.append(1)
        # await state.update_data(some_list=some_list)
        await message.answer("Позволька спросить, на что?", reply_markup=kb_key.coast_pyrpose)
      



        await Test.next()
        


@dp.message_handler(state=Test.q2)
async def answer_q2(message: types.Message, state:FSMContext):
    

    # Полученный ответ избавляем от пробелов и заносим в список
    cost_purpose_q2 = (message.text.strip()).split()[0] 

    # Удаление обычной клавиатуры:
    # markup = types.ReplyKeyboardRemove()
    # await bot.send_message(message.from_user.id, 'text', reply_markup=markup)

    # Обновляем данные
    await state.update_data(answer2=cost_purpose_q2)
    # Достаём переменные
    data = await state.get_data()
    
    # Не уверен, что это нужно:
    # answer = data.get("answer1")

    a = await message.answer("Спасибо, я всё записал 👌", reply_markup=types.ReplyKeyboardRemove())
    await bot.delete_message(message_id=a['message_id'], chat_id=message.from_user.id)
    await bot.send_message(text="Спасибо, я всё записал 👌", chat_id=message.from_user.id, reply_markup=kb_key.new_costs)
    
    
    data['answer1'] # Количество потраченных денег


    db.add_new_coast(message.from_user.id, count=data["answer1"], category=data["answer2"])
    db.update_money(message.from_user.id, money=data["answer1"])
    # Variant 1 для завершения
    # Это обязательно, чтобы закрыть state
    await state.finish()
    
    # Variant 2
    #await state.reset_state()

    #Variant 3 для завершения без стирания данных
    #await state.rest_state(wirh_data=False)

@dp.callback_query_handler(text="last_5_cost")
async def last_5_cost(message: types.Message):
    """Выгрузка последних 5-ти трат"""
    last_cost = db.last_5_coast(message.from_user.id)
    print(last_cost)
    await bot.edit_message_text(text=f"Последние 5 трат:\n\n{last_cost[0]}\n{last_cost[1]}\n{last_cost[2]}\n{last_cost[3]}\n{last_cost[4]}",
        chat_id=message.from_user.id,
        message_id=message.message.message_id,
        reply_markup=kb_key.new_costs
        )

@dp.callback_query_handler(text="today_cost")
async def today_cost(message: types.Message):
    """Выгрузка за сегодня"""
    await message.answer()
    today_costs = db.today_cost(message.from_user.id)
   
        # Создаём пустой список и проходим по каждому элементу tuple
        # Чтобы отобразить каждый элемент с новой строки в сообщении
    y = ""
    for i in today_costs:       
        i = str(i)
        y += ("\n" + i)

    await bot.edit_message_text(text=f"Траты за сегодня:\n\n{y}",
        chat_id=message.from_user.id,
        message_id=message.message.message_id,
        reply_markup=kb_key.new_costs
        )
        

@dp.callback_query_handler(text="all_cost")
async def today_cost(message: types.Message):
    """Выгрузка за всё время"""
    await message.answer()
    today_costs = db.all_cost(message.from_user.id)
   
        # Создаём пустой список и проходим по каждому элементу tuple
        # Чтобы отобразить каждый элемент с новой строки в сообщении
    y = ""
    for i in today_costs:       
        i = str(i)
        y += ("\n" + i)

    await bot.edit_message_text(text=f"Траты за всё время:\n\n{y}",
        chat_id=message.from_user.id,
        message_id=message.message.message_id,
        reply_markup=kb_key.new_costs
        )



@dp.callback_query_handler(text="yesterday_cost")
async def today_cost(message: types.Message):
    """Выгрузка за вчера"""
    await message.answer()
    yesterday_cost = db.yesterday_cost(message.from_user.id)
    print(db.yesterday_cost(message.from_user.id))

    y = ""
    for i in yesterday_cost:       
        i = str(i)
        y += ("\n" + i)

    await bot.edit_message_text(text=f"Траты за вчера:\n\n{y}",
        chat_id=message.from_user.id,
        message_id=message.message.message_id,
        reply_markup=kb_key.new_costs
        )



##################################################################
#                        
#                            Функции БД

#_________________________________________________________________

# Получаем данные фото, которое отправлено боту.
@dp.message_handler(content_types=['photo'])
async def scan_message(msg: types.Message):
    document_id = msg.photo[0].file_id
    file_info = await bot.get_file(document_id)
    print(f'file_id: {file_info.file_id}')
    print(f'file_path: {file_info.file_path}')
    print(f'file_size: {file_info.file_size}')
    print(f'file_unique_id: {file_info.file_unique_id}')
    file_db.file_record(file_info.file_id, file_info.file_path, 'photo', msg.from_user.id)
    print(f'Данные о файле успешно добавлены в БД')

# Получаем данные стикера, который отправлен боту.
@dp.message_handler(content_types=['sticker'])
async def scan_message(msg: types.Message):
    document_id = msg.sticker.file_id
    file_info = await bot.get_file(document_id)
    print(f'file_id: {file_info.file_id}')
    print(f'file_path: {file_info.file_path}')
    print(f'file_size: {file_info.file_size}')
    print(f'file_unique_id: {file_info.file_unique_id}')
    file_db.file_record(file_info.file_id, file_info.file_path, "sticker", msg.from_user.id)
    print(f'Данные о файле успешно добавлены в БД')



##################################################################
#_________________________________________________________________



# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

@dp.message_handler(commands="test2")
async def cmd_test1(message: types.Message):
    await message.answer("Test 2")




    # Фикс исключения с блокировкой сторонним пользователем бота
    # В дальнейшем надо заменить на "try...except"
@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
