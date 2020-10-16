#created:on:16 October 2020
#creator:author:Victor NKuna
#email:victor.nkuna@yahoo.com


def dates_2W_apart():
    print(""""Print ten dates .each two weeks aprat ,starting from the currrent date""")

    """System when HR,date people are going to be paid"""

    from datetime import datetime, timedelta
    dt =  datetime.today()
    x = 0
    while x<10:
        print(dt)
        dt=dt+timedelta(days=14)
        x=x+1
dates_2W_apart()


