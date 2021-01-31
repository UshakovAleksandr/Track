import datetime


class Task:
    """
    Класс "Задачи".
    Отвечает за создание событий и операций с ними.
    Включает в себя конструктор и классовый атрибут.
    """

    task_table_name = "current_tasks"

    def __init__(self, conn, date: str, event: str):
        self.conn = conn
        self.date = date
        self.event = event
        self.status = "to_be_done"

    def check_db_func(self):
        """
        Вспомогательный объектный метод.
        Отвечает за выборку из таблицы БД для проверки на входжение.
        Используется во множестве методов объекта класса.
        :return: метод возвращает объект класс List - список кортежей, в которых собраны все записи
        из таблий БД, по которому происходит проверка на вхождение.
        """

        cur = self.conn.cursor()

        query_select = f"SELECT * FROM {self.task_table_name}"
        check_lst = [row for row in cur.execute(query_select)]

        return check_lst

    def add_event(self):
        """
        Объектный метод.
        Отвечает за добавление события в таблицу БД, в список "активных событий".
        Принзак "активности" события для объекта указан и протавляется по умолчанию - "to_be_done".
        :return: метод ничего не возвращает.
        """
        cur = self.conn.cursor()

        if (self.date, self.event, self.status) not in Task.check_db_func(self):
            query_inset = f"INSERT INTO {self.task_table_name} VALUES(?, ?, ?)"
            cur.execute(query_inset, (self.date, self.event, self.status))
            self.conn.commit()

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

        cur = self.conn.cursor()

        if (self.date, self.event, self.status) in Task.check_db_func(self):
            query_update = f"UPDATE {self.task_table_name} SET status = ? WHERE date = ? AND event = ?"
            cur.execute(query_update, (new_status, self.date, self.event))
            self.conn.commit()
            print("Deleted successfully")
        else:
            print("Event not found")

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

        cur = self.conn.cursor()

        counter = 0
        for row in Task.check_db_func(self):
            if row[0] == self.date and row[2] == "to_be_done":
                query_update = f"UPDATE {self.task_table_name} SET status = ? WHERE date = ?"
                cur.execute(query_update, (new_status, self.date))
                self.conn.commit()
                counter += 1
        print(f"Deleted {counter} event" if counter == 1 else f"Deleted {counter} events")


class User:
    """
    Класс "Пользователь".
    Отвечает за операции печати и удаление объетов класса Task (событий).
    Включает в себя конструктор и классовый атрибут.
    """

    task_table_name = "current_tasks"

    def __init__(self, conn):
        self.conn = conn

    def print_event_by_date(self, date):
        """
        Объектный метод.
        Отвечает за печать всех событий за указанную дату и находящихся
        в списке "активных событий" (т.е. имеющих статус - "to_be_done").
        Резутат выводится в отсортированном виде.
        :param date: занчение, на которое требуется изменить дату.
        :return: метод ничего не возвращает.
        """

        cur = self.conn.cursor()

        query_select = f"SELECT event FROM {self.task_table_name} WHERE date = ? AND status = 'to_be_done'"
        event_lst = sorted([row[0] for row in cur.execute(query_select, (date, ))])

        if not event_lst:
            print("No events on this date")
        else:
            for event in event_lst:
                print(event)

    def print_all_events(self):
        """
        Объектный метод.
        Отвечает за печать всех событий находящихся
        в списке "активных событий" (т.е. имеющих статус - "to_be_done").
        Резутат выводится в отсортированном виде.
        Правится формат "даты" на указанный в ТЗ.
        Пример: если дата: 1-2-3, то вернется 0001-02-03
        :return: метод ничего не возвращает.
        """

        cur = self.conn.cursor()

        query_select = f"SELECT date, event FROM {self.task_table_name} WHERE status = 'to_be_done'"
        event_lst = sorted([row for row in cur.execute(query_select)])
        if not event_lst:
            print("No events")
        else:
            for event in event_lst:
                date = event[0].split("-")
                date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
                print(date, event[1])
