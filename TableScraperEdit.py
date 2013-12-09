from bs4 import BeautifulSoup
import urllib2

url = input('Paste the url you want to use: ')
css = input('What kind of tag are you looking for (class or id)?: ')
tag = input('What are the cells tagged as?: ')
file_name = input('What would you like to name the data file?: ')

site = url
page = urllib2.urlopen(site)
soup = BeautifulSoup(page)

cell1 = ""
cell2 = ""
cell3 = ""
cell4 = ""
cell5 = ""
cell6 = ""

table = soup.find("table", {css : tag})

f = open(file_name, 'w')

for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 2:
        cell1 = cells[0].find(text=True)
        cell2 = cells[1].find(text=True)
        result = cell1 + ";" + cell2 
        f.write(result)
       

    if len(cells) == 3:
        cell1 = cells[0].find(text=True)
        cell2 = cells[1].find(text=True)
        cell3 = cells[2].find(text=True)
        result = cell1 + ";" + cell2 + ";" + cell3 
        f.write(result)
       
 
    if len(cells) == 4:
        cell1 = cells[0].find(text=True)
        cell2 = cells[1].find(text=True)
        cell3 = cells[2].find(text=True)
	cell4 = cells[3].find(text=True)
	result = cell1 + ";" + cell2 + ";" + cell3 + ";" + cell4
	f.write(result)


    if len(cells) == 5:
        cell1 = cells[0].find(text=True)
        cell2 = cells[1].find(text=True)
        cell3 = cells[2].find(text=True)
	cell4 = cells[3].find(text=True)
	cell5 = cells[4].find(text=True)
        result = cell1 + ";" + cell2 + ";" + cell3 + ";" + cell4 + ":" + cell5 
        f.write(result)
     

    if len(cells) == 6:
        cell1 = cells[0].find(text=True)
        cell2 = cells[1].find(text=True)
        cell3 = cells[2].find(text=True)
        cell4 = cells[3].find(text=True)
        cell5 = cells[4].find(text=True)
	cell6 = cells[5].find(text=True)
        result = cell1 + ";" + cell2 + ";" + cell3 + ";" + cell4 + ":" + cell5 + ";" + cell6
        f.write(result)
        


f.close()
print "Done!"
