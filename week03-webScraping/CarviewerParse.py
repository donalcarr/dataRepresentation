from bs4 import BeautifulSoup 

with open("C:\\Users\\Donal\\Desktop\\Diploma\\Data Representation\\dataRepresentation\\week03-webScraping\\CarViewerLab1.html") as fp: 
    soup = BeautifulSoup(fp,'html.parser')

#print (soup.prettify())

rows = soup.findAll("tr") 

for row in rows: 

    print("------") 

print(row)