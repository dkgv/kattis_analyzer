# Kattis Analyzer

# Dependencies
The following packages are required to run the code and can be installed with pip:
```
pyfiglet
requests
BeautifulSoup4
```

# Usage
After cloning the repository, create `credentials.txt` in the root directory with your Kattis email and password formatted as `email:password`, and run `python katanalyzer.py`.

Alternatively, if you do not wish to store your login credentials, you can manually extract the `EduSiteCookie` cookie from Kattis. Simply sign in to Kattis as you normally would. When signed in, open the web developer menu and find the storage inspector (shortcut Shift+F9). In the bottom window you should now find a row containing with `EduSiteCookie`. Copy its value, create `sessionid.txt`, and paste it there. Run `python katanalyzer.py`.

To scrape your data from Kattis simply type `scrape` followed by enter.

To review the data scraped from Kattis, first run `scrape` and afterwards run `analyze`.

# Wishlist
* GUI baby
* Possibility to lookup if you are on any toplists in speed
* Program could suggest problems in the same score as your average/other parameters
