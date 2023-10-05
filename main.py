import requests
from bs4 import BeautifulSoup
from book import Book
from csv_books import write_csv

#Parse HTML response
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#Activate class Book to generate the data
category = []
book = Book().generate_data(url)
category.append(book)

write_csv(category)