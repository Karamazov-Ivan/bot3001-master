import sqlite3

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_users(self, status = True):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `users` WHERE `status` = ?", (status)).fetchall()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status = True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `status`) VALUES(?,?)", (user_id,status))

    def update_subscription(self, user_id, status):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()

#############################################################3

    def add_user(self, user_id, name, status = False):
        """Добавляем нового пользователя"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `status`, `name`) VALUES(?,?,?)", (user_id, status, name))

    def check_user(self, *user_id):
        """Проверяем наличие юера в базе"""
        with self.connection:
            return self.cursor.execute("SELECT DISTINCT `user_id` FROM `users` WHERE `user_id` = ?", (user_id)).fetchall()

    def cost_create_table(self, *user_id):
        """Создаём таблицу для конкретного юзера"""
        b = user_id
        print(f"Table for user {b[0]} is ready")
        with self.connection:
            return self.cursor.execute(f"CREATE TABLE `{b[0]}` ( `id` INTEGER NOT NULL \
                PRIMARY KEY AUTOINCREMENT, `count` INTEGER, `category` TEXT, \
                    `time` DATE_TIME DEFAULT CURRENT_TIMESTAMP, \
                        `date` DATE DEFAULT CURRENT_DATE)")

    def check_user_status(self, *user_id):
        """Проверяем наличие БД у юзера. Принимает id юзера, и его же возврщает в случа успеха"""
        with self.connection:
            return self.cursor.execute("SELECT DISTINCT `user_id` FROM `users` WHERE `user_id` = ? AND status = TRUE", (user_id)).fetchall()

    def update_user_status(self, user_id, status):
        """Обновляем статус пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def add_new_coast(self, *user_id, count, category):
        """Добавляем в личную БД информацию о расходах"""
        b = user_id
        with self.connection:
            return self.cursor.execute(f"INSERT INTO `{b[0]}` (`count`, `category`) VALUES(?,?)", (count, category))


    # Money:
    def update_money(self, user_id, money):
        """Обновляем значение денег у юзера"""
        with self.connection:
            return self.cursor.execute(f"UPDATE `users` SET `money` = ((SELECT `money` FROM `users` WHERE `user_id` = ?) + ?) WHERE `user_id` = ?", (user_id, money, user_id))

    def check_money(self, user_id):
            """Проверяем количество денег юзера"""
            with self.connection:
                return self.cursor.execute(f"SELECT `money` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()

    # Costs:
    def last_5_coast(self, *user_id):
        """Выбрать 5 последних записей
        DESC - сортирует в порядке убывания
        ASC - сортирует в порядк возрастания
        LIMIT - в данном случае возвращает первые 5 значений из отсортированного списка"""
        b = user_id
        with self.connection:
            return self.cursor.execute(f"SELECT `count`, `category` FROM `{b[0]}` ORDER BY `date` DESC LIMIT 5").fetchall()

    def today_cost(self, *user_id):
        """Выгразка данных за сегодня"""
        b = user_id
        with self.connection:
            return self.cursor.execute(f"SELECT `count`, `category` FROM `{b[0]}` WHERE `date` = (SELECT DATE((SELECT julianday()), 'localtime'))").fetchall()

    def yesterday_cost(self, *user_id):
        """Выгрузка данных за вчера"""
        b = user_id
        with self.connection:
            return self.cursor.execute(f"SELECT `count`, `category` FROM `{b[0]}` WHERE `date` = (SELECT DATE((SELECT julianday()-1), 'localtime'))").fetchall()
        	
    def all_cost(self, *user_id):
        """Выгрузка данных за всё время"""
        b = user_id
        with self.connection:
            return self.cursor.execute(f"SELECT `count`, `category` FROM `{b[0]}`").fetchall()
    
    
    # def week_cost(self, *user_id):
    #     """Выгрузка данных за неделю"""
    #     b = user_id
    #     with self.connection:
    #         return self.cursor.execute(f"SELECT `count`, `category` FROM `{b[0]}` WHERE `date` = (SELECT DATE((SELECT julianday()-1), 'localtime'))").fetchall()
            



class SQL_file_record:

    def __init__(self, database):
        """Подключамся к БД"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def file_record(self, file_id, file_path, category, user_id):
        """Добавляем id файла и его путь в БД"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `files` (`file_id`, `file_path`, `category`, `user_id`) VALUES(?,?,?,?)", (file_id, file_path, category, user_id))