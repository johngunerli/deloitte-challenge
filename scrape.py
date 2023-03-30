# we can scrape some of the key points for each thread here: https://gt-student-wiki.org/mediawiki/index.php/Thread


from bs4 import BeautifulSoup
import urllib.request



URL = 'https://gt-student-wiki.org/mediawiki/index.php/Thread'


# scrape this data, and put it into a html file 


scraped = urllib.request.urlopen(URL).read()


# this infomraiton is in a ul tag 

soup = BeautifulSoup(scraped, 'html.parser')

# find all ul tags 


ul_tags = soup.find_all('ul')

print(ul_tags)


    