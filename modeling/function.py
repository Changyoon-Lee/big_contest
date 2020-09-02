import pandas as pd
from datetime import timedelta
from datetime import date


def gu_lists():
    gu_l = [
        "노원구", "강서구", "광진구", "강동구", "도봉구", "관악구", "성북구", "구로구", "금천구", "동대문구", "영등포구",
        "서대문구", "중구", "강북구", "강남구", "송파구", "은평구", "종로구", "동작구", "성동구", "양천구", "중랑구",
        "서초구", "마포구", "용산구",
    ]
    return gu_l


def makefulldate():
    fulldate = pd.DataFrame(columns=["date"])
    start = date(2020, 2, 1)
    end = date(2020, 8, 31)
    for n in range(int((end - start).days) + 1):
        fulldate.loc[n, "date"] = start + timedelta(n)
    fulldate["date"] = pd.to_datetime(fulldate["date"])

    return fulldate


def make_sumcount(df, col_name="확진자 수", last_nday=7):
    df["sumcount"] = 0
    for i in range(len(df)):
        if i < last_nday:
            df["sumcount"][i] = sum(df[col_name][:i])
        else:
            df["sumcount"][i] = sum(df[col_name][i - last_nday : i])
    return df
