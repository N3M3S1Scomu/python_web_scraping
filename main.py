from bs4 import BeautifulSoup
import requests
url="https://www.imdb.com/chart/top/"
r=requests.get(url) #siteyi açar
soup=BeautifulSoup(r.text,"html.parser") # sets web infos
imdb_list=soup.find("tbody",{"class":"lister-list"}).find_all("tr")
i=0
for film in imdb_list:
    i=(i+1)
    name=film.find("td",{"class":"titleColumn"}).a.text
    hist=film.find("td",{"class":"titleColumn"}).span.text.strip("()")
    rating=film.find("td",{"class":"ratingColumn imdbRating"}).strong.text
    str_i=str(i)
    print(str_i,"-",name,"-",hist,"-",rating)



