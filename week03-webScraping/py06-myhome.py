  
##requests library used to retrieve url##
import requests
import csv
##Beautiful Soup is a program used for parsing HTML##
from bs4 import BeautifulSoup
url = "https://www.myhome.ie/residential/mayo/property-for-sale?page=1"
page = requests.get(url)
##parses page into DOM format##
soup = BeautifulSoup(page.content, 'html.parser')
##open a CSV file to write contents of myhome results##
home_file = open('C:\\Users\\Donal\\Desktop\\Diploma\\Data Representation\\dataRepresentation\\week03-webScraping\\week03MyHome.csv', mode='w') 
##format of CSV tab delimited and doesn't treat quotes as commas##
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
##finds div tag to retrieve property details
listings = soup.findAll("div", class_="PropertyListingCard" )

##loops through class and returns price and address##
for listing in listings:
    entryList = []
    
    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)

    home_writer.writerow(entryList)
home_file.close()