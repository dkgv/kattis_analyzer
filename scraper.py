from bs4 import BeautifulSoup
import requests

output = open('KattisData.txt','a+', encoding='utf-8')
headers = {
    "Cookie": "__cfduid=dfe5e7e244a9017fcdf40f89b18486a501567024193; site24x7rumID=892557796277259.1567987468145; __zlcmid=u0iUpiPIr8kFxM; EduSiteCookie=7f75652d-6127-4b16-a99c-9cd5caae06a4"
}

url, page = "https://open.kattis.com/problems?page=", 0
print("Reading page: ", flush=True, end='')
while True:
    req = requests.get(url + str(page), headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    print(f"{page}..", flush=True,end='')
    results = 0
    page += 1
    for row in soup.find('table').find('tbody').find_all('tr'):
        results += 1
        vals, cl = row.find_all('td'), row.get('class')
        output.write('###'.join([vals[x].text for x in range(9)]) + '###' + (str(cl[1]) if len(cl) > 1 else 'unsolved') + '\n')
    if results == 0:
        break
print('done')
output.flush()
output.close()
