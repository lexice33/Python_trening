import pandas as pd
import requests
start_date = str(input('Введите дату начала отсчета в формате (дд.мм.гггг): '))
end_date = str(input('Введите дату конца отсчета в формате (дд.мм.гггг): '))

daterange = pd.bdate_range(start=start_date, end=end_date)
# Затем вы можете выполнить цикл по дате, чтобы распечатать дату:

list_date = []

for single_date in daterange:
    list_date.append(single_date.strftime("%Y%m%d"))


list_kurs_usd = []
index_list_date = 0
for i in range(len(list_date)):
    req_usd = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/'
                           f'exchange?valcode=USD&date={list_date[index_list_date]}&json').json()
    print(req_usd)
    list_kurs_usd.append(req_usd[0]["rate"])
    index_list_date = index_list_date + 1
print(sum(list_kurs_usd) / len(list_kurs_usd))


# m = 0
# for i in range(len(list_kurs_usd)):
#     sr_usd = float(list_kurs_usd[m]) + 0
#     m = m + 1
# print(sr_usd)
