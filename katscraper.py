import requests
import os
import platform
import time
from bs4 import BeautifulSoup


def scrape(email, password):
    save_to_file = "kattis-latest.txt"
    output = open(save_to_file, "a+", encoding="utf-8")
    headers = { "Cookie": "EduSiteCookie=" }

    if email and password:
        headers["Cookie"] += get_session_id(email, password) + ";"
    else:
        headers["Cookie"] += open("sessionid.txt").readline() + ";"

    url = "https://open.kattis.com/problems?page="
    page = 0
    print("scraping (this will take approximately 30 seconds)")
    while True:
        req = requests.get(url + str(page), headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        print("{}..".format(page), flush=True, end='')
        results = 0
        page += 1
        for row in soup.find('table').find('tbody').find_all('tr'):
            results += 1
            vals, cl = row.find_all('td'), row.get('class')
            output.write(
                '###'.join([vals[x].text for x in range(9)]) + '###' + (str(cl[1]) if len(cl) > 1 else 'unsolved') + '\n')
        if results == 0:
            break

    output.flush()
    output.close()

    print(" ")      #dont ask.. just leave it!
    print("scraping completed. Data saved to " + save_to_file)


def get_session_id(email, password):
    s = requests.Session()
    url = "https://open.kattis.com/login/email?"
    r = s.get(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://open.kattis.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": url,
        "Upgrade-Insecure-Requests": "1",
    }
    soup = BeautifulSoup(r.text, "html.parser")
    token = soup.find("input", {"name": "csrf_token"}).attrs.get("value")
    data = {
        "csrf_token": token,
        "user": email,
        "password": password,
        "submit": "Submit"
    }
    s.post(url, headers=headers, data=data)
    return s.cookies.get_dict()["EduSiteCookie"]
