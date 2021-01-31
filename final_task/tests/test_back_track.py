import pytest
import sqlite3
from track.back_track import Task
from track.back_track import User


@pytest.fixture()
def db_connection():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    QUERY_CREATE = "CREATE TABLE IF NOT EXISTS current_tasks (date TEXT, event TEXT, status TEXT)"
    cur.execute(QUERY_CREATE)
    conn.commit()

    cur.close()

    yield conn

    conn.close()


def test_check_db_func(db_connection):

    """
    Тест проверяет корректность работы метода check_db_func():
    Метод add-event() - используется для добавления в БД
    :param db_connection: фикстура для создание БД in memory
    """

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    t = Task(db_connection, test_date1, test_event1)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done")]

    test_date2 = "2019-2-2"
    test_event2 = "Сходитьвмагазин2"
    t = Task(db_connection, test_date2, test_event2)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done"),
                                 (test_date2, test_event2, "to_be_done")]

    test_date3 = "2019-3-3"
    test_event3 = "Сходитьвмагазин3"
    t = Task(db_connection, test_date3, test_event3)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done"),
                                 (test_date2, test_event2, "to_be_done"),
                                 (test_date3, test_event3, "to_be_done")]

    test_date4 = "2019-4-4"
    test_event4 = "Сходитьвмагазин4"
    t = Task(db_connection, test_date4, test_event4)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done"),
                                 (test_date2, test_event2, "to_be_done"),
                                 (test_date3, test_event3, "to_be_done"),
                                 (test_date4, test_event4, "to_be_done")]

    test_date5 = "2019-5-5"
    test_event5 = "Сходитьвмагазин5"
    t = Task(db_connection, test_date5, test_event5)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done"),
                                 (test_date2, test_event2, "to_be_done"),
                                 (test_date3, test_event3, "to_be_done"),
                                 (test_date4, test_event4, "to_be_done"),
                                 (test_date5, test_event5, "to_be_done")]

    test_date6 = "2019-6-6"
    test_event6 = "Сходитьвмагазин6"
    t = Task(db_connection, test_date6, test_event6)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done"),
                                 (test_date2, test_event2, "to_be_done"),
                                 (test_date3, test_event3, "to_be_done"),
                                 (test_date4, test_event4, "to_be_done"),
                                 (test_date5, test_event5, "to_be_done"),
                                 (test_date6, test_event6, "to_be_done")]

    test_date7 = "2019-7-7"
    test_event7 = "Сходитьвмагазин7"
    t = Task(db_connection, test_date7, test_event7)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done"),
                                 (test_date2, test_event2, "to_be_done"),
                                 (test_date3, test_event3, "to_be_done"),
                                 (test_date4, test_event4, "to_be_done"),
                                 (test_date5, test_event5, "to_be_done"),
                                 (test_date6, test_event6, "to_be_done"),
                                 (test_date7, test_event7, "to_be_done")]

    test_date8 = "2019-8-8"
    test_event8 = "Сходитьвмагазин8"
    t = Task(db_connection, test_date8, test_event8)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done"),
                                 (test_date2, test_event2, "to_be_done"),
                                 (test_date3, test_event3, "to_be_done"),
                                 (test_date4, test_event4, "to_be_done"),
                                 (test_date5, test_event5, "to_be_done"),
                                 (test_date6, test_event6, "to_be_done"),
                                 (test_date7, test_event7, "to_be_done"),
                                 (test_date8, test_event8, "to_be_done")]

    test_date9 = "2019-9-9"
    test_event9 = "Сходитьвмагазин9"
    t = Task(db_connection, test_date9, test_event9)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done"),
                                 (test_date2, test_event2, "to_be_done"),
                                 (test_date3, test_event3, "to_be_done"),
                                 (test_date4, test_event4, "to_be_done"),
                                 (test_date5, test_event5, "to_be_done"),
                                 (test_date6, test_event6, "to_be_done"),
                                 (test_date7, test_event7, "to_be_done"),
                                 (test_date8, test_event8, "to_be_done"),
                                 (test_date9, test_event9, "to_be_done")]

    test_date10 = "2019-10-10"
    test_event10 = "Сходитьвмагазин10"
    t = Task(db_connection, test_date10, test_event10)
    t.add_event()
    assert t.check_db_func() == [(test_date1, test_event1, "to_be_done"),
                                 (test_date2, test_event2, "to_be_done"),
                                 (test_date3, test_event3, "to_be_done"),
                                 (test_date4, test_event4, "to_be_done"),
                                 (test_date5, test_event5, "to_be_done"),
                                 (test_date6, test_event6, "to_be_done"),
                                 (test_date7, test_event7, "to_be_done"),
                                 (test_date8, test_event8, "to_be_done"),
                                 (test_date9, test_event9, "to_be_done"),
                                 (test_date10, test_event10, "to_be_done")]


def test_event_update_to_done(db_connection, capsys):
    """
    Тест проверяет корректность работы метода event_update_to_done():
    add-event() - используется для добавления в БД
    :param db_connection: фикстура для создание БД in memory
     :param capsys: требуется для методов, которые ничего не возвращают, но печатают
    """

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    t = Task(db_connection, test_date1, test_event1)
    t.add_event()
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted successfully" + "\n"

    test_date2 = "2019-2-2"
    test_event2 = "Сходитьвмагазин2"
    t = Task(db_connection, test_date2, test_event2)
    t.add_event()
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted successfully" + "\n"

    test_date3 = "2019-3-3"
    test_event3 = "Сходитьвмагазин3"
    t = Task(db_connection, test_date3, test_event3)
    t.add_event()
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted successfully" + "\n"

    test_date4 = "2019-4-4"
    test_event4 = "Сходитьвмагазин4"
    t = Task(db_connection, test_date4, test_event4)
    t.add_event()
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted successfully" + "\n"

    test_date5 = "2019-5-5"
    test_event5 = "Сходитьвмагазин5"
    t = Task(db_connection, test_date5, test_event5)
    t.add_event()
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted successfully" + "\n"

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    t = Task(db_connection, test_date1, test_event1)
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Event not found" + "\n"

    test_date2 = "2019-2-2"
    test_event2 = "Сходитьвмагазин2"
    t = Task(db_connection, test_date2, test_event2)
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Event not found" + "\n"

    test_date3 = "2019-3-3"
    test_event3 = "Сходитьвмагазин3"
    t = Task(db_connection, test_date3, test_event3)
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Event not found" + "\n"

    test_date4 = "2019-4-4"
    test_event4 = "Сходитьвмагазин4"
    t = Task(db_connection, test_date4, test_event4)
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Event not found" + "\n"

    test_date5 = "2019-5-5"
    test_event5 = "Сходитьвмагазин5"
    t = Task(db_connection, test_date5, test_event5)
    t.event_update_to_done("done")
    out, _ = capsys.readouterr()
    assert out == "Event not found" + "\n"


def test_event_update_by_date(db_connection, capsys):
    """
    Тест проверяет корректность работы метода event_update_by_date():
    add-event() - используется для добавления в БД
    :param db_connection: фикстура для создание БД in memory
    :param capsys: требуется для методов, которые ничего не возвращают, но печатают
    """

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    t = Task(db_connection, test_date1, test_event1)
    t.add_event()
    t.event_update_by_date("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted 1 event" + "\n"

    test_date2 = "2019-2-2"
    test_event2 = "Сходитьвмагазин2"
    t = Task(db_connection, test_date2, test_event2)
    t.add_event()
    t.event_update_by_date("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted 1 event" + "\n"

    test_date3 = "2019-3-3"
    test_event3 = "Сходитьвмагазин3"
    t = Task(db_connection, test_date3, test_event3)
    t.add_event()
    t.event_update_by_date("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted 1 event" + "\n"

    test_date4 = "2019-4-4"
    test_event4 = "Сходитьвмагазин4"
    t = Task(db_connection, test_date4, test_event4)
    t.add_event()
    t.event_update_by_date("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted 1 event" + "\n"

    test_date5 = "2019-5-5"
    test_event5 = "Сходитьвмагазин5"
    t = Task(db_connection, test_date5, test_event5)
    t.add_event()
    t.event_update_by_date("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted 1 event" + "\n"

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    test_event2 = "Сходитьвмагазин2"
    t1 = Task(db_connection, test_date1, test_event1)
    t2 = Task(db_connection, test_date1, test_event2)
    t1.add_event()
    t2.add_event()
    t1.event_update_by_date("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted 2 events" + "\n"

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    test_event2 = "Сходитьвмагазин2"
    test_event3 = "Сходитьвмагазин3"
    t1 = Task(db_connection, test_date1, test_event1)
    t2 = Task(db_connection, test_date1, test_event2)
    t3 = Task(db_connection, test_date1, test_event3)
    t1.add_event()
    t2.add_event()
    t3.add_event()
    t1.event_update_by_date("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted 3 events" + "\n"

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    test_event2 = "Сходитьвмагазин2"
    test_event3 = "Сходитьвмагазин3"
    test_event4 = "Сходитьвмагазин4"
    t1 = Task(db_connection, test_date1, test_event1)
    t2 = Task(db_connection, test_date1, test_event2)
    t3 = Task(db_connection, test_date1, test_event3)
    t4 = Task(db_connection, test_date1, test_event4)
    t1.add_event()
    t2.add_event()
    t3.add_event()
    t4.add_event()
    t1.event_update_by_date("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted 4 events" + "\n"

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    t1 = Task(db_connection, test_date1, test_event1)
    t1.event_update_by_date("done")
    out, _ = capsys.readouterr()
    assert out == "Deleted 0 events" + "\n"


def test_print_event_by_date(db_connection, capsys):
    """
    Тест проверяет корректность работы метода test_print_event_by_date():
    add-event() - используется для добавления в БД
    :param db_connection: фикстура для создание БД in memory
    :param capsys: требуется для методов, которые ничего не возвращают, но печатают
    """

    u = User(db_connection)
    u.print_event_by_date("2019-1-1")
    out, _ = capsys.readouterr()
    assert out == "No events on this date" + "\n"

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    t = Task(db_connection, test_date1, test_event1)
    t.add_event()
    u = User(db_connection)
    u.print_event_by_date("2019-1-1")
    out, _ = capsys.readouterr()
    assert out == "Сходитьвмагазин1" + "\n"

    test_event2 = "Сходитьвмагазин2"
    t = Task(db_connection, test_date1, test_event2)
    t.add_event()
    u = User(db_connection)
    u.print_event_by_date("2019-1-1")
    out, _ = capsys.readouterr()
    assert out == "Сходитьвмагазин1\nСходитьвмагазин2" + "\n"

    test_event3 = "Сходитьвмагазин3"
    t = Task(db_connection, test_date1, test_event3)
    t.add_event()
    u = User(db_connection)
    u.print_event_by_date("2019-1-1")
    out, _ = capsys.readouterr()
    assert out == "Сходитьвмагазин1\nСходитьвмагазин2\nСходитьвмагазин3" + "\n"

    test_event4 = "Сходитьвмагазин4"
    t = Task(db_connection, test_date1, test_event4)
    t.add_event()
    u = User(db_connection)
    u.print_event_by_date("2019-1-1")
    out, _ = capsys.readouterr()
    assert out == "Сходитьвмагазин1\nСходитьвмагазин2\nСходитьвмагазин3\nСходитьвмагазин4" + "\n"

    test_event5 = "Сходитьвмагазин5"
    t = Task(db_connection, test_date1, test_event5)
    t.add_event()
    u = User(db_connection)
    u.print_event_by_date("2019-1-1")
    out, _ = capsys.readouterr()
    assert out == "Сходитьвмагазин1\nСходитьвмагазин2\nСходитьвмагазин3\nСходитьвмагазин4" \
                  "\nСходитьвмагазин5" + "\n"

    test_date2 = "2019-2-2"
    test_event6 = "Сходитьвмагазин6"
    t = Task(db_connection, test_date2, test_event6)
    t.add_event()
    u = User(db_connection)
    u.print_event_by_date("2019-2-2")
    out, _ = capsys.readouterr()
    assert out == "Сходитьвмагазин6" + "\n"

    test_event7 = "Сходитьвмагазин7"
    t = Task(db_connection, test_date2, test_event7)
    t.add_event()
    u = User(db_connection)
    u.print_event_by_date("2019-2-2")
    out, _ = capsys.readouterr()
    assert out == "Сходитьвмагазин6\nСходитьвмагазин7" + "\n"

    test_event8 = "Сходитьвмагазин8"
    t = Task(db_connection, test_date2, test_event8)
    t.add_event()
    u = User(db_connection)
    u.print_event_by_date("2019-2-2")
    out, _ = capsys.readouterr()
    assert out == "Сходитьвмагазин6\nСходитьвмагазин7\nСходитьвмагазин8" + "\n"

    test_event9 = "Сходитьвмагазин9"
    t = Task(db_connection, test_date2, test_event9)
    t.add_event()
    u = User(db_connection)
    u.print_event_by_date("2019-2-2")
    out, _ = capsys.readouterr()
    assert out == "Сходитьвмагазин6\nСходитьвмагазин7\nСходитьвмагазин8\nСходитьвмагазин9" + "\n"


def test_print_all_events(db_connection, capsys):
    """
    Тест проверяет корректность работы метода test_print_all_events():
    add-event() - используется для добавления в БД
    :param db_connection: фикстура для создание БД in memory
    :param capsys: требуется для методов, которые ничего не возвращают, но печатают
    """

    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "No events" + "\n"

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    t = Task(db_connection, test_date1, test_event1)
    t.add_event()
    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "2019-01-01 Сходитьвмагазин1" + "\n"

    test_date2 = "2019-2-2"
    test_event2 = "Сходитьвмагазин2"
    t = Task(db_connection, test_date2, test_event2)
    t.add_event()
    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "2019-01-01 Сходитьвмагазин1\n2019-02-02 Сходитьвмагазин2" + "\n"

    test_date3 = "2019-3-3"
    test_event3 = "Сходитьвмагазин3"
    t = Task(db_connection, test_date3, test_event3)
    t.add_event()
    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "2019-01-01 Сходитьвмагазин1\n2019-02-02 Сходитьвмагазин2" \
                  "\n2019-03-03 Сходитьвмагазин3" + "\n"

    test_date4 = "2019-4-4"
    test_event4 = "Сходитьвмагазин4"
    t = Task(db_connection, test_date4, test_event4)
    t.add_event()
    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "2019-01-01 Сходитьвмагазин1\n2019-02-02 Сходитьвмагазин2" \
                  "\n2019-03-03 Сходитьвмагазин3\n2019-04-04 Сходитьвмагазин4" + "\n"

    test_date5 = "2019-5-5"
    test_event5 = "Сходитьвмагазин5"
    t = Task(db_connection, test_date5, test_event5)
    t.add_event()
    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "2019-01-01 Сходитьвмагазин1\n2019-02-02 Сходитьвмагазин2" \
                  "\n2019-03-03 Сходитьвмагазин3\n2019-04-04 Сходитьвмагазин4" \
                  "\n2019-05-05 Сходитьвмагазин5" + "\n"

    test_date1 = "2019-1-1"
    test_event1 = "Сходитьвмагазин1"
    t = Task(db_connection, test_date1, test_event1)
    t.add_event()
    test_date2 = "2019-2-2"
    test_event2 = "Сходитьвмагазин2"
    t = Task(db_connection, test_date2, test_event2)
    t.add_event()
    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "2019-01-01 Сходитьвмагазин1\n2019-02-02 Сходитьвмагазин2" \
                  "\n2019-03-03 Сходитьвмагазин3\n2019-04-04 Сходитьвмагазин4" \
                  "\n2019-05-05 Сходитьвмагазин5" + "\n"

    test_date3 = "2019-3-3"
    test_event3 = "Сходитьвмагазин3"
    t = Task(db_connection, test_date3, test_event3)
    t.add_event()
    test_date4 = "2019-4-4"
    test_event4 = "Сходитьвмагазин4"
    t = Task(db_connection, test_date4, test_event4)
    t.add_event()
    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "2019-01-01 Сходитьвмагазин1\n2019-02-02 Сходитьвмагазин2" \
                  "\n2019-03-03 Сходитьвмагазин3\n2019-04-04 Сходитьвмагазин4" \
                  "\n2019-05-05 Сходитьвмагазин5" + "\n"

    test_date5 = "2019-5-5"
    test_event5 = "Сходитьвмагазин5"
    t = Task(db_connection, test_date5, test_event5)
    t.add_event()
    test_date6 = "2019-6-6"
    test_event6 = "Сходитьвмагазин6"
    t = Task(db_connection, test_date6, test_event6)
    t.add_event()
    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "2019-01-01 Сходитьвмагазин1\n2019-02-02 Сходитьвмагазин2" \
                  "\n2019-03-03 Сходитьвмагазин3\n2019-04-04 Сходитьвмагазин4" \
                  "\n2019-05-05 Сходитьвмагазин5\n2019-06-06 Сходитьвмагазин6" + "\n"

    test_date7 = "2019-7-7"
    test_event7 = "Сходитьвмагазин7"
    t = Task(db_connection, test_date7, test_event7)
    t.add_event()
    test_date8 = "2019-8-8"
    test_event8 = "Сходитьвмагазин8"
    t = Task(db_connection, test_date8, test_event8)
    t.add_event()
    u = User(db_connection)
    u.print_all_events()
    out, _ = capsys.readouterr()
    assert out == "2019-01-01 Сходитьвмагазин1\n2019-02-02 Сходитьвмагазин2" \
                  "\n2019-03-03 Сходитьвмагазин3\n2019-04-04 Сходитьвмагазин4" \
                  "\n2019-05-05 Сходитьвмагазин5\n2019-06-06 Сходитьвмагазин6" \
                  "\n2019-07-07 Сходитьвмагазин7\n2019-08-08 Сходитьвмагазин8" + "\n"
