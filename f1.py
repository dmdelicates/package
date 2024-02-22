from datetime import datetime, date

def cur_d():
    return datetime.date(datetime.today())

def low(l1):
    l2 = []
    for l in l1:
        l2.append(datetime.isoweekday(l))
    return l2
