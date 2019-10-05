# Kattis Analyzer

# Dependencies
The following packages is required to run the code:
```
pyfiglet
requests
BeautifulSoup4
```

#Usage
To run this code you need to make sure the modules in the dependencies list is installed.

Before running the code you need to generate a session ID on kattis end input it into the sessionid.txt file. To find this ID simply log on to kattis as you would normally do it in your favorite browser. While logged in go in the web developer menu and find the storage inspector(shortcut shift+F9). In the window in the bottom you should now find a value in the EduSiteCookie row. Copy this value into the sessionid.txt file.

With the session id in place you run the kattisanalizer.py file to start the program.

To scrape you data from kattis simply type scrape followed by enter.

To review the data scraped from kattis type parse followed by enter after the scrape is complete. 

# ToDo
* Parser could load custom or just latest data
* Guide for people to find their session id for the scraper
* Rewrite parser in python
* Cookie extraction if possible
* MOAR STATS!

# Suggestions(may need discussion)
* Possibility to lookup if you are on any toplists in speed
* Program could suggest problems in the same score as your average/other parameters

# Wishlist

* GUI baby
* Smart login
