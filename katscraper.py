from bs4 import BeautifulSoup
import requests
import sqlite3
import os
import platform
import time

def scrape():
    savetofile = getfilename()
    output = open(savetofile,"a+", encoding="utf-8")

    headers = {
        "Cookie": "EduSiteCookie="+getsessionsid()+";"
    }

    url = "https://open.kattis.com/problems?page="
    page = 0
    print("scraping (this will take approximately 30 seconds)")
    while True:
        req = requests.get(url + str(page), headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        print(".", flush=True, end = " ")
        results = 0
        page += 1
        for row in soup.find("table").find("tbody").find_all("tr"):
            results += 1
            vals, cl = row.find_all("td"), row.get("class")
            output.write("###".join([vals[x].text for x in range(9)]) + "###" + (str(cl[1]) if len(cl) > 1 else "unsolved") + "\n")
        if results == 0:
            break

    output.flush()
    output.close()

    print(" ")      #dont ask.. just leave it!
    print("scraping completed. Data saved to " + savetofile)
    return savetofile


# Gets the current time and returns it with a filename
def getfilename():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = "kattisdata-"+timestamp+".txt"
    return filename

def getsessionsid():
    cookieid = open("sessionid.txt", "r")
    return cookieid.read()
