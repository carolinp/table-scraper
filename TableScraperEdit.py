#Imports the libraries we'll be using. Make sure you have these installed
#first by typing import into python and seeing if it does anything
from bs4 import BeautifulSoup
import urllib2

#These are the editable variables in the scraper. The user defines them by
#typing their answers to the input questions in quotation marks.
url = input('Paste the url you want to use: ')
css = input('What kind of tag are you looking for (class or id)?: ')
tag = input('What are the cells tagged as?: ')
file_name = input('What would you like to name the data file?: ')

#Defining and opening the site that will be used
site = url
page = urllib2.urlopen(site)
soup = BeautifulSoup(page)

#Empty variables that the data from each cell will go into later
cell1 = ""
cell2 = ""
cell3 = ""
cell4 = ""
cell5 = ""
cell6 = ""

#Defines what we're looking for (a table) and what the table we're looking for
#is tagged as - either a css class or id that's defined by the user
table = soup.find("table", {css : tag})

#Opens the file that the data will go into and gives it a filename defined 
#by the user
f = open(file_name, 'w')

#Iterates through each row in the table to find each cell
for row in table.findAll("tr"):
    cells = row.findAll("td")

#Defines the number of cells we're looking for, finds the text in each of 
#those cells, and makes the empty variables from earlier equal to the text.
#Right now, the scraper can scrape tables with up to six columns.Then it writes
#to the file in the csv format, with each cell surrounded by semicolons
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
        

#Closes the file and prints to let the user know that it's done
f.close()
print "Done!"
