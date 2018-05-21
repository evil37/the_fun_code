# coded by evil37

import os

os.mkdir("wallpaper")
os.chdir("wallpaper")
for i in range(1, 7278):
    import urllib

    import requests
    from bs4 import BeautifulSoup

    url = "https://wallpaperscraft.com/all/page{}".format(i)

    res = requests.request("GET", url)

    soup = BeautifulSoup(res.content, "html.parser")

    wallpaper_link_list = soup.find("div", {"class": "content-main"}).findAll("a", class_="wallpapers__link")


    def get_wallpaper(name):
        return "https://images.wallpaperscraft.com/image/{}_1920x1080.jpg".format(name)


    for x in wallpaper_link_list:
        link = str((x["href"]))
        wallpaper_link = (get_wallpaper(link))
        print(wallpaper_link)
        print(link)
        urllib.request.urlretrieve(wallpaper_link, "{}.jpg".format(link.replace("/", "")))
