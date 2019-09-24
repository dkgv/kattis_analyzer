from bs4 import BeautifulSoup
import requests
import sqlite3
import os
import platform

# Function that finds the path for a given file
def find_path(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

username = os.getlogin()

# Find the path of the cookie database for the given system
if (platform.system() == 'Darwin'):
    path = find_path('cookies.sqlite','/Users/'+ username + '/Library/Application Support/Firefox/Profiles')
elif (platform.system() == 'Linux'):
    print("Find the path for the file cookis.sqlite!")

# Connect to the database and fetch the cookies
con = sqlite3.connect(path)
cur = con.cursor()
cur.execute("select * from moz_cookies where host = '.kattis.com'")
cookies = cur.fetchall()

first = cookies[0][4]
second = cookies[1][4]

output = open('KattisData.txt','a+', encoding='utf-8')

headers = {
    "Cookie": "__cfduid=" + first + "; __zlcmid=" + second + "; EduSiteCookie=5b4fc553-af51-4548-94ce-0934705ecac5;"
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
