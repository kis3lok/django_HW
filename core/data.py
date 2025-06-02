masters = [
    {"id": 1, "name": "James Alan Hetfield"},
    {"id": 2, "name": "Anthony 'Tony' Kiedis"},
    {"id": 3, "name": "Serj Tankian"},
    {"id": 4, "name": "William Frederick Durst"},
    {"id": 5, "name": "Jonathan Howsmon Davis"},
]


# Список возможных услуг барбершопа
services = [
    "Стрижка под 'Горшок'",
    "Укладка 'Взрыв на макаронной фабрике'",
    "Королевское бритье опасной бритвой",
    "Окрашивание 'Жизнь в розовом цвете'",
    "Мытье головы 'Душ впечатлений'",
    "Стрижка бороды 'Боярин'",
    "Массаж головы 'Озарение'",
    "Укладка 'Ветер в голове'",
    "Плетение косичек 'Викинг'",
    "Полировка лысины до блеска"
]

# Статусы заявок
STATUS_NEW = 'новая'
STATUS_CONFIRMED = 'подтвержденная'
STATUS_CANCELLED = 'отмененная'
STATUS_COMPLETED = 'выполненная'

# Тестовые данные заявок
orders = [
    {
        "id": 1,
        "client_name": "Михаил Горшенёв",
        "services": ["Стрижка под 'Горшок'", "Полировка лысины до блеска"],
        "master_id": 1,
        "date": "2025-03-20",
        "status": STATUS_NEW
    },
    {
        "id": 2,
        "client_name": "Алексей Горшенёв",
        "services": ["Укладка 'Взрыв на макаронной фабрике'"],
        "master_id": 2,
        "date": "2025-03-21",
        "status": STATUS_CONFIRMED
    },
    {
        "id": 3,
        "client_name": "Валерий Кипелов",
        "services": ["Королевское бритье опасной бритвой", "Стрижка бороды 'Боярин'", "Массаж головы 'Озарение'"],
        "master_id": 3,
        "date": "2025-03-19",
        "status": STATUS_COMPLETED
    },
    {
        "id": 4,
        "client_name": "Chester Charles Bennington",
        "services": ["Окрашивание 'Жизнь в розовом цвете'", "Укладка 'Ветер в голове'"],
        "master_id": 4,
        "date": "2025-03-22",
        "status": STATUS_CANCELLED
    },
    {
        "id": 5,
        "client_name": "Kurt Donald Cobain",
        "services": ["Плетение косичек 'Викинг'", "Стрижка бороды 'Боярин'"],
        "master_id": 5,
        "date": "2025-03-23",
        "status": STATUS_NEW
    },
    {
        "id": 6,
        "client_name": "Клаус Майне",
        "services": ["Полировка лысины до блеска", "Массаж головы 'Озарение'"],
        "master_id": 1,
        "date": "2025-03-24",
        "status": STATUS_CONFIRMED
    },
    {
        "id": 7,
        "client_name": "Долорес Мери Эйлин О’Риордан",
        "services": ["Укладка 'Ветер в голове'", "Мытье головы 'Душ впечатлений'"],
        "master_id": 2,
        "date": "2025-03-25",
        "status": STATUS_CANCELLED
    },
    {
        "id": 8,
        "client_name": "Джон Майкл Осборн",
        "services": ["Укладка 'Взрыв на макаронной фабрике'", "Массаж головы 'Озарение'", "Мытье головы 'Душ впечатлений'"],
        "master_id": 3,
        "date": "2025-03-26",
        "status": STATUS_COMPLETED
    },
    {
        "id": 9,
        "client_name": "Phil Anselmo",
        "services": ["Королевское бритье опасной бритвой"],
        "master_id": 4,
        "date": "2025-03-27",
        "status": STATUS_NEW
    },
    {
        "id": 10,
        "client_name": "Corey Taylor",
        "services": ["Стрижка бороды 'Боярин'", "Плетение косичек 'Викинг'", "Массаж головы 'Озарение'"],
        "master_id": 5,
        "date": "2025-03-28",
        "status": STATUS_COMPLETED
    }
]