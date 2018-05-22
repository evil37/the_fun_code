# coded by evil37

import os
import urllib
import requests
from bs4 import BeautifulSoup
try:
    os.mkdir("wallpaper")
    os.chdir("wallpaper")
except:
    pass

print("~evil37~")
print("Downloading images [*]")
for i in range(1, 7278):
   

    print("Downloading ({}/7277) ({}%)".format(i,("{0:.2f}".format(((i/7277)*100)))))
    url = "https://wallpaperscraft.com/all/page{}".format(i)

    res = requests.request("GET", url)

    soup = BeautifulSoup(res.content, "html.parser")

    wallpaper_link_list = soup.find("div", {"class": "content-main"}).findAll("a", class_="wallpapers__link")


    def get_wallpaper(name):
        return "https://images.wallpaperscraft.com/image/{}_1920x1080.jpg".format(name)


    for x in wallpaper_link_list:
        link = str((x["href"]))
        wallpaper_link = (get_wallpaper(link))
        print("Downloaded {}".format(link.split("/")[2]))
        urllib.request.urlretrieve(wallpaper_link, "{}.jpg".format(link.replace("/", "")))
        
