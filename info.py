#Удаление сообщения:

# @dp.callback_query_handler(text="тут название твоей callback_data")
#     async def call_main_menu(call: CallbackQuery):
#     await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id) 





# inline_btn_1 = InlineKeyboardButton('кнопка 1', callback_data='btn1')

# # row_width=1 - Ширина клавиатуры
# inline_kb_full = InlineKeyboardMarkup(row_width=1).add(inline_btn_1)

# inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
# inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
# inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')

# inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
# inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)

# inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
# inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
# inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
# inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
# inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))


				# Хэндлеры:
		#_________________________


# @dp.callback_query_handler(lambda c: c.data == 'start')
# async def callback(message: Message):
#     await bot.send_message(
#         chat_id=message.from_user.id,
#         reply_markup=feel_good_kb,
#         text="отлично")

                                # @dp.message_handler(Command('menu'))
                                # async def show_menu(message:types.Message):
                                #     await list_categories(message)


                                # async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
                                #     markup = categories_keyboard()

                                # @dp.callback_query_handler(menu_cd.filter())
                                # async def navigate(call: types.CallbackQuery, callback_data: dict):
                                #     current_level = callback_data.get('level')
                                #     category = callback_data.get('subcategory')
                                #     item_id = callback_data.get('item_id')
                                    
                                #     levels = {
                                #         '0': list_categories,
                                        
                                #     }






# async def edit_msg(message: types.Message):
#     await bot.edit_message_text("Так")
    
# не позволяет модифицировать сообщения
#with suppress(MessageNotModified):


# @dp.callback_query_handler(lambda f: f.data == "buy_premium")
# async def buy_premium(call: greet_main_kb):
#     await call.answer(cache_time=60,text="⏳")
 
#     text = [
#         '<b>Премиум-аккаунт</b>',
#         'Активируйте премиум-аккаунт чтобы использовать всю мощь бота.',
#         '',
#         'Приобретая  ������  вы получаете следующие преимущества:',
#         '',
#         '<b>Преимущество 1</b>: блаблабла',
#         '',
#         '<b>Преимущество 2</b>: блаблабла',
#         '',
#         '<b>Выберите более подходящее для вас предложение:</b>',
#         '<em>Тут должны быть инлайн-кнопки</em>'
#     ]
#     await call.message.edit_text('\n'.join(text), reply_markup=buy_premium_buttons)






# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
# async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
#     code = callback_query.data[-1]
#     if code.isdigit():
#         code = int(code)
#     if code == 2:
#         await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
#     elif code == 5:
#         await bot.answer_callback_query(
#             callback_query.id,
#             text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
#     else:
#         await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')


# #Отправляет все возможные кнопки
# @dp.message_handler(commands=['2'])
# async def process_command_2(message: types.Message):
#     await message.reply("Отправляю все возможные кнопки", reply_markup=inline_kb_full)


#_____________________________________________________________________________________________________

# @dp.callback_query_handler(lambda c: c.data == 'start_button2')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, callback_data= dp.message_handler() )



# @dp.message_handler(commands=['1'])
# async def process_command_1(message: types.Message):
#     await message.reply("Первая инлайн кнопка", reply_markup=inline_kb1)

# @dp.message_handler(commands='iq')
# async def process_hi1_command(message: types.Message):
#     await message.answer(text="Меню:", reply_markup=greet_start_kb)


# @dp.message_handler(commands=['hi'])
# async def process_hi1_command(message: types.Message):
#     await message.reply("Первое - изменяем размер клавиатуры", reply_markup=greet_kb)






# await bot.send_message(text="Ты первый", reply_markup=kb_key.button_bone, chat_id=call.from_user.id)

# @dp.message_handler(lambda message: emoji.demojize(message.text) == ':game_die:')
# async def text_handler(message: types.Message):
#     print("ok")
#     await bot.send_message(text="Ты первый", reply_markup=kb_key.button_bone, chat_id=message.from_user.id)



# @dp.message_handler(text="lol")
# async def gaming(message: types.Message):
#     await bot.send_message(text="Ты первый", reply_markup=kb_key.button_bone, chat_id=message.from_user.id)
                


# Кнопка игры


# @dp.callback_query_handler(text="game")
# async def game(call: types.CallbackQuery):
#     await bot.send_message("Во что играем?", reply_markup=kb_key.game_kb)



# @dp.message_handler(commands="test4")
# async def with_hidden_link(message: types.Message):
#     await message.answer(
#         f"{fmt.hide_link('https://telegram.org/blog/video-calls/ru')}Кто бы мог подумать, что "
#         f"в 2020 году в Telegram появятся видеозвонки!\n\nОбычные голосовые вызовы "
#         f"возникли в Telegram лишь в 2017, заметно позже своих конкурентов. А спустя три года, "
#         f"когда огромное количество людей на планете приучились работать из дома из-за эпидемии "
#         f"коронавируса, команда Павла Дурова не растерялась и сделала качественные "
#         f"видеозвонки на WebRTC!\n\nP.S. а ещё ходят слухи про демонстрацию своего экрана :)",
#         parse_mode=types.ParseMode.HTML)



# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     msg = text(bold('Я могу ответить на следующие команды:'),
#                '/voice', '/photo', '/group', '/note', '/file, /testpre', sep='\n')
#     await message.reply(msg, parse_mode='MARKDOWN')





# @dp.message_handler(commands=['start12'])
# async def bones(message: types.Message):
#     # keyboard_markup = types.InlineKeyboardMarkup()
#     # user_id_btn = types.InlineKeyboardButton('Получить ID пользывателя из Inline кнопки', callback_data= 'user_id')
#     # keyboard_markup.row(user_id_btn)
#     # await message.answer(f"Ваш ID: {message.from_user.id}", reply_markup=keyboard_markup)
#     a = await bot.send_dice(emoji='🎲', chat_id=message.from_user.id)
#     print(a)
#     print(message.message_id)
#     print(a['dice']['value'])


                                                    # import logging

                                                    # from aiogram import Bot, types
                                                    # from aiogram.utils import executor
                                                    # from aiogram.dispatcher import Dispatcher
                                                    # from aiogram.contrib.fsm_storage.memory import MemoryStorage
                                                    # from aiogram.contrib.middlewares.logging import LoggingMiddleware

                                                    # from config import TOKEN
                                                    # from utils import TestStates
                                                    # from messages import MESSAGES


                                                    # logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                                                    #                     level=logging.DEBUG)


                                                    # bot = Bot(token=TOKEN)
                                                    # dp = Dispatcher(bot, storage=MemoryStorage())

                                                    # dp.middleware.setup(LoggingMiddleware())


                                                    # @dp.message_handler(commands=['start'])
                                                    # async def process_start_command(message: types.Message):
                                                    #     await message.reply(MESSAGES['start'])


                                                    # @dp.message_handler(commands=['help'])
                                                    # async def process_help_command(message: types.Message):
                                                    #     await message.reply(MESSAGES['help'])


                                                    # @dp.message_handler(state='*', commands=['setstate'])
                                                    # async def process_setstate_command(message: types.Message):
                                                    #     argument = message.get_args()
                                                    #     state = dp.current_state(user=message.from_user.id)
                                                    #     if not argument:
                                                    #         await state.reset_state()
                                                    #         return await message.reply(MESSAGES['state_reset'])

                                                    #     if (not argument.isdigit()) or (not int(argument) < len(TestStates.all())):
                                                    #         return await message.reply(MESSAGES['invalid_key'].format(key=argument))

                                                    #     await state.set_state(TestStates.all()[int(argument)])
                                                    #     await message.reply(MESSAGES['state_change'], reply=False)


                                                    # @dp.message_handler(state=TestStates.TEST_STATE_1)
                                                    # async def first_test_state_case_met(message: types.Message):
                                                    #     await message.reply('Первый!', reply=False)


                                                    # @dp.message_handler(state=TestStates.TEST_STATE_2[0])
                                                    # async def second_test_state_case_met(message: types.Message):
                                                    #     await message.reply('Второй!', reply=False)


                                                    # @dp.message_handler(state=TestStates.TEST_STATE_3 | TestStates.TEST_STATE_4)
                                                    # async def third_or_fourth_test_state_case_met(message: types.Message):
                                                    #     await message.reply('Третий или четвертый!', reply=False)


                                                    # @dp.message_handler(state=TestStates.all())
                                                    # async def some_test_state_case_met(message: types.Message):
                                                    #     with dp.current_state(user=message.from_user.id) as state:
                                                    #         text = MESSAGES['current_state'].format(
                                                    #             current_state=await state.get_state(),
                                                    #             states=TestStates.all()
                                                    #         )
                                                    #     await message.reply(text, reply=False)


                                                    # @dp.message_handler()
                                                    # async def echo_message(msg: types.Message):
                                                    #     await bot.send_message(msg.from_user.id, msg.text)


                                                    # async def shutdown(dispatcher: Dispatcher):
                                                    #     await dispatcher.storage.close()
                                                    #     await dispatcher.storage.wait_closed()


                                                    # if __name__ == '__main__':
                                                    #     executor.start_polling(dp, on_shutdown=shutdown)

    # Удаление обычной клавиатуры:
    # markup = types.ReplyKeyboardRemove()
    # await bot.send_message(message.from_user.id, 'text', reply_markup=markup)




# @dp.message_handler(state=Test.q2)
# async def answer_q2(message:types.Message, state:FSMContext):

#     cost_purpose_q2 = message.text

#     if not (cost_purpose_q2.isalpha()):
#         await bot.send_message(text="Допускается только одно слово! 😡", chat_id=message.from_user.id,)
#         await Test.q2.set()

#     else:

#         # Обновляем данные
#         await state.update_data(answer2=cost_purpose_q2)
#         # Достаём переменные
#         data = await state.get_data()
        
#         # Не уверне, что это нужно:
#         # answer = data.get("answer1", "answer2")
    
#         await message.answer("Спасибо, я всё записал 👌", reply_markup=kb_key.new_costs)
        
#         #Variant 1 для завершения
#         # Это обязательно, чтобы закрыть state
#         await state.finish()


#         print(data)
        
#         # Variant 2
#         #await state.reset_state()

#         #Variant 3 для завершения без стирания данных
#         #await state.rest_state(wirh_data=False)

# # Порядок handlers важен!!!!

# # Для кнопки отмена или назад
# # @dp.message_handler(state="*")
# # async def all_handlets(message: types.Message, state:FSMContext):
    

    # Удаление обычной клавиатуры:
    # markup = types.ReplyKeyboardRemove()
    # await bot.send_message(message.from_user.id, 'text', reply_markup=markup)

# Установка пакетов:
# ~$ python3.9 -m pip install bs4
# pip install --upgrade Pillow


from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    q1 = State()
    q2 = State()

class Game(StatesGroup):
    g1 = State()

class Slot(StatesGroup):
    s1 = State()
