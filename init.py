rom bs4 import BeautifulSoup
import urllib2
site = "http://www.grammy.com/nominees/search?artist=&field_nominee_work_value=$
page = urllib2.urlopen(site)
soup = BeautifulSoup(page)

year = ""
category = ""
performer = ""
work = ""
table = soup.find("table", {"class" : "views-table cols-4"})

f = open('output.csv', 'w')

for row in table.findAll("tr"):
    cells = row.findAll("td")

   if len(cells) == 4:
        year = cells[0].find(text=True)
        category = cells[1].find(text=True)
        work = cells[2].find(text=True)
        for cells[3] in row.findAll("p"):
            link = cells[3].findAll("a")
            if len(link) == 1:
                performer = link[0].find(text=True)
            elif len(link) == 0:
                performer = cells[3].find(text=True)
        result = year + "," + category + "," + work + "," + performer
        print result
        f.write(result)

f.close()
