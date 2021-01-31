import sys
import sqlite3
from track.back_track import Task
from track.back_track import User


def main():

    print("Трекер задач")
    print("*" * 44)
    print("""
Для начала работы введите команду 'StartApp'
Для оканчания работы введите команду 'Quit'\n""")

    """
    Создается БД и таблица.
    """

    conn = sqlite3.connect("tracker.db")
    cur = conn.cursor()

    QUERY_CREATE = "CREATE TABLE IF NOT EXISTS current_tasks (date TEXT, event TEXT, status TEXT)"
    cur.execute(QUERY_CREATE)
    conn.commit()

    cur.close()

# User.del_all_from_table()
# User.print_all_from_table()

    while True:

        start = input("Введите команду (StartApp/Quit): ")

        if start.lower() == "startapp":

            while True:

                task_input = input("Введите команду, дату и событие: ").split()

                if len(task_input) > 1:
                    data_check = [int(i) for i in task_input[1].split("-")]
                    if data_check[0] > 0 and 0 < data_check[1] <= 12 and 0 < data_check[2] <= 31:
                        if task_input[0] == "Add":
                            task = Task(conn, task_input[1], task_input[2])
                            task.add_event()
                        elif len(task_input) > 2 and task_input[0] == "Del":
                            task = Task(conn, task_input[1], task_input[2])
                            task.event_update_to_done("done")
                        elif len(task_input) == 2 and task_input[0] == "Del":
                            task = Task(conn, task_input[1], "")
                            task.event_update_by_date("done")
                        elif len(task_input) == 2 and task_input[0] == "Find":
                            user = User(conn)
                            user.print_event_by_date(task_input[1])
                    else:
                        print("Указана неверная дата")
                else:
                    if not task_input:
                        print("Некорректный формат ввода!")
                        continue
                    elif task_input[0].lower() == "print":
                        user = User(conn)
                        user.print_all_events()
                    else:
                        print("\nПрограмма завершила свою работу.")
                        sys.exit()
        elif start.lower() == "quit":
            print("\nПрограмма завершила свою работу.")
            sys.exit()
        else:
            print("Указана неверная команда!")
            continue

    conn.close()


if __name__ == '__main__':
    main()

# add_event() - ДОБАВИТЬ ДАТУ И СОБЫТИЕ
# Add 2019-1-1 Сходитьвмагазин
# Add 2019-7-12 Помытьмашину
# Add 2019-1-1 Поехатьнадачу
# Add 2019-12-1 Сходитьвмагазин

# event_update_to_done() - ОТМЕТИТЬ СОБЫТИЕ КАК ВЫПОЛНЕНОЕ И УБРАТЬ ИЗ СПИСКА АКТУАЛЬНЫХ
# Del 2019-1-1 Сходитьвмагазин
# Del 2019-7-12 Помытьмашину
# Del 2019-1-1 Поехатьнадачу
# Del 2019-12-1 Сходитьвмагазин

# event_update_by_date() - ВЫПОЛНИТЬ СОБЫТИЯ ЗА ДАТУ
# Del 2019-1-1
# Del 2019-7-12
# Del 2019-12-1

# print_event_by_date() - НАЙТИ СОБЫТИЯ ЗА ДАТУ
# Find 2019-1-1
# Find 2019-7-12
# Find 2019-12-1

# Print - ПОСМОТРЕТЬ ВСЕ АКТУАЛЬНЫЕ
# Quit
