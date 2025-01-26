from datetime import datetime,timedelta

from_time = datetime.now()
searchtime = from_time + timedelta(days=180)
date_from = from_time.strftime("%d/%m/%Y"),   #搜尋開始時間
data_to = searchtime.strftime("%d/%m/%Y"),    #搜尋結束時間

print(date_from)
print(data_to)


[{'city': 'Jeju Island',
  'from': '01/05/2024',
  'iataCode': 'CJU',
  'id': 2,
  'lowestPrice': 54,
  'out': '',
  'return': '',
  'to': '01/07/2024'},
 {'city': 'Amsterdam',
  'from': '01/08/2024',
  'iataCode': 'AMS',
  'id': 3,
  'lowestPrice': '',
  'out': '',
  'return': ''}]