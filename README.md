table-scraper
=============
Do you need a data set? Are you lazy (I sure am!)? This table scraper can make it easier for you. By just answering a few prompt questions from the command line, you can easily scrape HTML tables from a website.

##Getting Started

So first, let's look at what the files do:

TableScraperScript.py: This is a scraper that I made to get some data off the Grammy's website. If you're working on a similar project and want to fork and edit it to suit your needs, awesome! Go right ahead. Otherwise, it may not be totally useful to you other than to serve as an example of how to build your own scraper. But I did use this template to build...

TableScraperEdit.py: This is sort of a global version of this scraper. If you run it in the command line and answer the questions it prompts you with, you can scrape HTML tables on the web. If this is what you're interested in using, you don't actually need the other files.

output.xml: The edited data set that TableScraperScript.py gave me.

Alright, so let's get started! First, download any files you want, just make sure you get TableScraperEdit.py. 

Next, make sure you've got BeautifulSoup downloaded (if not, do `apt-get python-bs4` or `pip install beautifulsoup4`).

Then, open up a window with the site you want to scrape and go ahead and inspect all up in the table you want to scrape (right click "Inspect Element"). 

Open a terminal window and enter in `python TableScraperEdit.py` (if you've downloaded the whole folder, make sure you enter `cd table-scraper` first). Now it's going to ask you a bunch of questions -- they're not terribly difficult but it's important to remember to PUT ALL OF YOUR ANSWERS IN QUOTATION MARKS. Otherwise, the program will get confused and cry little error tears all over you and you'll have to run the script again. Now, let's go through the questions: 

Paste the url you want to use: Pretty easy. Just copy the url from the website you're scraping from, paste it in the terminal, put quotes around it and press enter. For example, I used search results from the Grammys winners website for my project, so I did "http://www.grammy.com/nominees/search?artist=&field_nominee_work_value=&year=All&genre=31". 

What kind of tag are you looking for (class or id)?: Now we're starting to identify the table that the script should be looking through. This is where you should enter the table's css selector, usually either a class or an id. Here's what my table looks like in the element inspector: 
![What my table looks like in the element inspector](https://lh4.googleusercontent.com/-Yyfoe9VCJCI/UqitDWC5zeI/AAAAAAAAAQ4/QCpcx8Jg1dM/w1035-h223-no/silshack.JPG)

So I'll enter "class".

What are the cells tagged as?: This means entering the specific class or id of your table. For example, you'll see that if you look up at the picture of my table's HTML, the class is "views-table cols-4", so that's what I'll enter.

What would you like to name the data file?: This not only determines the file's name but also its format. Right now, it's just a choice between xml and csv, so choose one of those formats and enter a name. For example, I entered "output.xml". 

The terminal should print out that the data is writing for a little bit, and then that'll tell you that it's done. Go look for your file, and it should be there! 

##Contributor Guidelines

This little project is just getting its legs, so please, feel free to contribute regardless of your level as a programmer! I only ask that you:
* Be respectful of others. Use comments for constructive criticsm or positive remarks.
* Do commits in your own fork and send me a pull request to merge any changes.
* If you find an issue, please be descriptive - make sure to note what file the issue is in and what lines of code need to be fixed.
* This project is primarily written in Python, so please indent with four spaces. Also, be descriptve by naming variables by what they do and by frequently using comments.



