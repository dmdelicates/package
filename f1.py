import random
from datetime import datetime, date
def gen_list():
    l = []
    for i in range(5):
        l.append(date(day=random.randint(1,28),month=random.randint(1,12),year=random.randint(1980, 2024)))
    return l
def cur_d():
    return datetime.date(datetime.today())