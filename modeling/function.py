from datetime import timedelta
from datetime import date

import pickle
import pandas as pd

class DFyoon:
    def __init__(self):
        with open('data/역넣으면구나오는dict.pickle', 'rb') as f:
            self.station_gu_dic = pickle.load(f)

        self.df_junguk = pd.read_pickle('data/전국확진자수.pickle')
        with open('data/구별확진자수dict.pickle', 'rb') as f:
            self.dic_gu_count=pickle.load(f)
            print('불러오기완료')

        self.gu_list = [
            "노원구", "강서구", "광진구", "강동구", "도봉구", "관악구", "성북구", "구로구", "금천구", "동대문구", "영등포구",
            "서대문구", "중구", "강북구", "강남구", "송파구", "은평구", "종로구", "동작구", "성동구", "양천구", "중랑구",
            "서초구", "마포구", "용산구",
            ]
        self.station_list = [i for i in self.station_gu_dic.keys()]
    
    def sta_merg(self, station, last_nday=7):
        try:
            df1 = make_sumcount(self.dic_gu_count[self.station_gu_dic[station]], last_nday=last_nday)[['date', 'sumcount']]
            df2 = make_sumcount(self.df_junguk, last_nday=last_nday)[['sumcount']]
            self.df_merged = pd.merge(df1,df2, on = 'date', how='left')
            self.df_merged.fillna(0,inplace = True)
            self.df_merged.columns=['date', '행정구역_확진자', '전국_확진자']
            return self.df_merged
        except:
            print(station)
        

    

# 20200201~20200831까지 날짜 생성
def makefulldate():
    fulldate = pd.DataFrame(columns=["date"])
    start = date(2020, 2, 1)
    end = date(2020, 5, 31)
    for n in range(int((end - start).days) + 1):
        fulldate.loc[n, "date"] = start + timedelta(n)
    fulldate["date"] = pd.to_datetime(fulldate["date"])

    return fulldate

#특정column의 지난 n일의 합계를 계산하여 새로운 sumcount를 만든다 
def make_sumcount(df, col_name="확진자 수", last_nday=7):
    df["sumcount"] = 0
    for i in range(len(df)):
        if i < last_nday:
            df["sumcount"][i] = sum(df[col_name][:i])
        else:
            df["sumcount"][i] = sum(df[col_name][i - last_nday : i])
    return df

def makefulldate2():
    fulldate = pd.DataFrame(columns=["date"])
    start = date(2019, 12, 1)
    end = date(2020, 5, 31)
    for n in range(int((end - start).days) + 1):
        fulldate.loc[n, "date"] = start + timedelta(n)
    fulldate["date"] = pd.to_datetime(fulldate["date"])

    return fulldate