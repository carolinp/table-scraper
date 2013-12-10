#Imports the libraries we'll be using. Make sure you have these installed
#first
from bs4 import BeautifulSoup
import urllib2

#Defines the webpage that we'll be scraping from
address = ["http://www.grammy.com/nominees/search?page=1&artist=&field_nominee_work_value=&year=All&genre=31", "http://www.grammy.com/nominees/search?page=2&artist=&field_nominee_work_value=&year=All&genre=31", "http://www.grammy.com/nominees/search?page=3&artist=&field_nominee_work_value=&year=All&genre=31", "http://www.grammy.com/nominees/search?page=4&artist=&field_nominee_work_value=&year=All&genre=31", "http://www.grammy.com/nominees/search?page=5&artist=&field_nominee_work_value=&year=All&genre=31"]
x = 0
#Opens the file that the data will go into and defines the file format/name
f = open('output.xml', 'w')
for i in address:
    site = address[x]
    page = urllib2.urlopen(site)
    soup = BeautifulSoup(page)
    print site
#Empty variables that the data from each cell will go into later
    year = ""
    category = ""
    performer = ""
    work = ""

#Defines what we're looking for (a table) and what it's tagged as so it can
#easily be found (in this case, a specific css class)
    table = soup.find("table", {"class" : "views-table cols-4"})

#Iterates through each row in the table to find each cell
    for row in table.findAll("tr"):
        cells = row.findAll("td")

#Defines the number of cells we're looking for, finds the text in each of 
#those cells, and makes the empty variables from earlier equal to the text
        if len(cells) == 4:
            year = cells[0].find(text=True)
            category = cells[1].find(text=True)
            work = cells[2].find(text=True)
#This particular cell was a little wonky and had text housed in either a 
#paragraph or a link, so I went through each of these cells and told it to
#find the text in either a link or a paragraph tag
	    for cells[3] in row.findAll("p"):
	        link = cells[3].findAll("a")
                if len(link) == 1:
	            performer = link[0].find(text=True)
	        elif len(link) == 0:
	            performer = cells[3].find(text=True)
#Writes to the file in the xml format, with each cell surrounded by tags and 
#prints to let us know that it's finished
        f.write("<dataTable>" + "<year>" + year + "</year>" + "<category>" + category + "</category>" + "<work>" + work + "</work>" + "<performer>" + performer + "</performer>" + "</dataTable>")
        print year    
    x += 1	

#Closes the file
f.close()
