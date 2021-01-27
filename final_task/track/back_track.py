import sqlite3
import datetime


class Task:
    """
    Класс "Задачи".
    Отвечает за создание событий и операций с ними.
    Включает в себя конструктор и классовые атрибуты.
    """

    data_base = "tracker.db"
    task_table_name = "current_tasks"

    def __init__(self, date: str, event: str):
        self.date = date
        self.event = event
        self.status = "to_be_done"

    @classmethod
    def check_db_func(cls):
        """
        Вспомогательный классовый метод.
        Отвечает за выборку из таблицы БД для проверки на входжение.
        Используется во множестве методов объекта класса.
        :return: метод возвращает объект класс List - список кортежей, в которых собраны все записи
        из таблий БД, по которому происходит проверка на вхождение.
        """
        conn = sqlite3.connect(cls.data_base)
        cur = conn.cursor()

        query_select = f"SELECT * FROM {cls.task_table_name}"
        check_lst = [row for row in cur.execute(query_select)]

        cur.close()
        conn.close()

        return check_lst

    def add_event(self):
        """
        Объектный метод.
        Отвечает за добавление события в таблицу БД, в список "активных событий".
        Принзак "активности" события для объекта указан и протавляется по умолчанию - "to_be_done".
        :return: метод ничего не возвращает.
        """
        conn = sqlite3.connect(self.data_base)
        cur = conn.cursor()

        if (self.date, self.event, self.status) not in Task.check_db_func():
            query_inset = f"INSERT INTO {self.task_table_name} VALUES(?, ?, ?)"
            cur.execute(query_inset, (self.date, self.event, self.status))
            conn.commit()

        cur.close()
        conn.close()

    def event_update_to_done(self, new_status: str):
        """
        Объектный метод.
        Отвечает за исключение события из списка "активных событий" и перемещение события
        в список "выполненых событий" путем изменения статуса с "to_be_done" на "done".
        Событие не удаляется из таблицы БД и доступно к просмотру отдельным классовым методом
        print_all_from_table() класса User.
        :param new_status: "done" - занчение, на которое требуется изменить статус.
        :return: метод ничего не возвращает.
        """
        conn = sqlite3.connect(self.data_base)
        cur = conn.cursor()

        if (self.date, self.event, self.status) in Task.check_db_func():
            query_update = f"UPDATE {self.task_table_name} SET status = ? WHERE date = ? AND event = ?"
            cur.execute(query_update, (new_status, self.date, self.event))
            conn.commit()
            print("Deleted successfully")
        else:
            print("Event not found")

        cur.close()
        conn.close()

    def event_update_by_date(self, new_status: str):
        """
        Объектный метод.
        Отвечает за исключения события(ий) из списка "активных событий" и перемещение события(ий)
        в список "выполненых событий" путем изменения статуса с "to_be_done" на "done"
        за указанную дату.
        Событие не удаляется из таблицы БД и доступно к просмотру отдельным классовым методом
        print_all_from_table() класса User.
        :param new_status: "done" - занчение, на которое требуется изменить статус
        :return: метод ничего не возвращает.
        """
        conn = sqlite3.connect(self.data_base)
        cur = conn.cursor()

        counter = 0
        for row in Task.check_db_func():
            if row[0] == self.date and row[2] == "to_be_done":
                query_update = f"UPDATE {self.task_table_name} SET status = ? WHERE date = ?"
                cur.execute(query_update, (new_status, self.date))
                conn.commit()
                counter += 1
        print(f"Deleted {counter} event" if counter == 1 else f"Deleted {counter} events")

        cur.close()
        conn.close()


class User:
    """
    Класс "Пользователь".
    Отвечает за операции печати и удаление объетов класса Task (событий).
    Не имеет конструктора.
    Имеет классовые атрибуты.
    Содержит исключительно классовые методы.
    """

    data_base = "tracker.db"
    task_table_name = "current_tasks"

    @classmethod
    def print_event_by_date(cls, date):
        """
        Классовый метод.
        Отвечает за печать всех событий за указанную дату и находящихся
        в списке "активных событий" (т.е. имеющих статус - "to_be_done").
        Резутат выводится в отсортированном виде.
        :param date: занчение, на которое требуется изменить дату.
        :return: метод ничего не возвращает.
        """
        conn = sqlite3.connect(cls.data_base)
        cur = conn.cursor()

        query_select = f"SELECT event FROM {cls.task_table_name} WHERE date = ? AND status = 'to_be_done'"
        event_lst = sorted([row[0] for row in cur.execute(query_select, (date, ))])

        if not event_lst:
            print("No events on this date")
        else:
            for event in event_lst:
                print(event)

        cur.close()
        conn.close()

    @classmethod
    def print_all_events(cls):
        """
        Классовый метод.
        Отвечает за печать всех событий находящихся
        в списке "активных событий" (т.е. имеющих статус - "to_be_done").
        Резутат выводится в отсортированном виде.
        Правится формат "даты" на указанный в ТЗ.
        Пример: если дата: 1-2-3, то вернется 0001-02-03
        :return: метод ничего не возвращает.
        """
        conn = sqlite3.connect(cls.data_base)
        cur = conn.cursor()

        query_select = f"SELECT date, event FROM {cls.task_table_name} WHERE status = 'to_be_done'"
        event_lst = sorted([row for row in cur.execute(query_select)])
        if not event_lst:
            print("No events")
        else:
            for event in event_lst:
                date = event[0].split("-")
                date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
                print(date, event[1])

        cur.close()
        conn.close()

    @classmethod
    def print_all_from_table(cls):
        """
        НЕ ПО ТЗ.
        Классовый метод.
        Временный, технический метод, печатает все записи таблицы БД, вне зависимости от статуса.
        :return: метод ничего не возвращает.
        """
        conn = sqlite3.connect(cls.data_base)
        cur = conn.cursor()

        query_select = f"SELECT * FROM {cls.task_table_name}"
        for row in cur.execute(query_select):
            print(row)

        cur.close()
        conn.close()

    @classmethod
    def del_all_from_table(cls):
        """
        НЕ ПО ТЗ.
        Классовый метод.
        Временный, технический метод, удаляет все записи таблицы БД.
        :return:
        """
        conn = sqlite3.connect(cls.data_base)
        cur = conn.cursor()

        query_delete = f"DELETE FROM {cls.task_table_name}"
        cur.execute(query_delete)
        conn.commit()

        cur.close()
        conn.close()
