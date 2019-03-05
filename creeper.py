#from the module installed by "python install beautifulsoup4" import it from the module
from bs4 import BeautifulSoup
#also import requests from Python's "core"??
import requests
#var called URL, and it is a input from user
url = input("Enter a website to extract the URL's from: ")
#var r to use requests get method and append our user input
r  = requests.get("http://" +url)
#var for data text
data = r.text
#make the soup using html.parser to get rid of warning for other machines
soup = BeautifulSoup(data, features="html.parser")

#for each link in soup get the href
for link in soup.find_all('a'):
    print(link.get('href'))