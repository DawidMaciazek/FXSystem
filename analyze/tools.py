import pandas as pd

def week_open_close_dif(df):
    # time EST without day light savings
    # open at 17:00:00 (hour, minute)
    weekday_flag = df.index.weekday == 6
    hour_flag = df.index.hour == 17
    minute_flag = df.index.minute == 0

    opening = df[hour_flag & minute_flag & weekday_flag]

    # close at 16:59:00 (hour, minute)
    weekday_flag = df.index.weekday == 4
    hour_flag = df.index.hour == 16
    minute_flag = df.index.minute == 59

    closing = df[hour_flag & minute_flag & weekday_flag]
    return (opening, closing)
