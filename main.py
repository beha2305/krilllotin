# 2-masala


# import requests
# import json
# url = 'https://github.com/annexare/Countries/blob/main/dist/countries.min.json'
# response = requests.get(url)
# languages = input('Tilni kiriting: ')
# if response.status_code==200:
#     data = response.json()
#     data=data['payload']['blob']['rawLines']
#     new_data = json.loads(data[0])
#     for i,j in new_data.items():
#         j['languages']=str(j['languages'])
#         # print(j['languages'])
#         if languages in j['languages']:
#             print(j['name'])
# else:
#     print('bu url ishlamayapti')



# 3-masala


# import requests
# import json
# url='https://nbu.uz/uz/exchange-rates/json/'
# response=requests.get(url)
# valyuta = {'1': 'USD>UZS','2':'UZS>USD','3':'RUB>UZS','4':'UZS>RUB'}
# pul_miqdori = int(input('Pul miqdorini kiriting: '))
# valyuta_almashtirish_raqami= int(input('Tugmani bosin: '))
# data =response.json()
# if response.status_code==200:
#     for i in range(len(data)):
#         if valyuta_almashtirish_raqami==1:
#             if data[i]['title']=='AQSh dollari':
#                 print(float(data[i]['nbu_buy_price'])*pul_miqdori)
#         if valyuta_almashtirish_raqami==2:
#             if data[i]['title']=='AQSh dollari':
#                 print(pul_miqdori/float(data[i]['nbu_cell_price']))
#         if valyuta_almashtirish_raqami==3:
#             if data[i]['title']=='RUB':
#                 print(float(data[i]['nbu_buy_price'])*pul_miqdori)
#         if valyuta_almashtirish_raqami==2:
#             if data[i]['title']=='RUB':
#                 print(pul_miqdori/float(data[i]['nbu_cell_price']))