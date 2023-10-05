from bs4 import BeautifulSoup
import requests
from lxml import html
import os


class Book:
    
    #mettre url en attribut de classe
    
    def get_soup(self, url):
        """
        Return --> soup, used to parse HTML content
        """
        response = requests.get(url, headers= {"accept-language" : "en-US"})
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup


    def title(self, url):
        """
        Scrap the book titles
        """
        soup = self.get_soup(url)
        return {'title' : soup.find("h1").string}


    def upc(self, url):
        """
        Scrap upc from the tag 'td' of the HTML class 'table table-striped'
        """
        soup = self.get_soup(url)
        extract_td = soup.find(class_= "table table-striped").find("td")
        
        return {
            "universal_product_code(upc)" : extract_td.string.strip('£')
            }


    def prices(self, url) : 
        """
        Scrap the book prices (excluding and including taxes)
        """
        soup = self.get_soup(url)
        extract_td = soup.find(class_= "table table-striped").find_all("td")
        
        return {
            "price_excluding_tax" : extract_td[2].string.strip('£'),
            "price_including_tax" : extract_td[3].string.strip('£')
        }

    def availability(self, url) : 
        """
        Scrap the book avaibilities
        """
        soup = self.get_soup(url)
        extract_td = soup.find(class_= "table table-striped").find_all("td")
        
        return {
            "number_available" : extract_td[5].string
        }


    def description(self, url) : 
        """
        Scrap the book description
        Variables :
            response : get the server response from the request
            tree : get and parse the HTML content
            p_text : extract text from the specific paragraphs
        Return a dict
        """
        response = requests.get(url, headers= {"accept-language" : "en-US"})
        tree = html.fromstring(response.text)
        p_text = tree.xpath("//*[@id='content_inner']/article/p/text()")
        
        return {
            "product_description" : p_text[0] if p_text else "Description non disponible"
        }
        
        
    def category(self, url) : 
        """
        Scrap the book category
        """
        soup = self.get_soup(url)
        extract_ul = soup.ul.find_all("a")
        category_text = extract_ul[-1].text if extract_ul else "Description non disponible"
        
        return {"category" : category_text}


    def reviews(self, url):
        """
        Scrap the book reviews
        """
        review = ""
        soup = self.get_soup(url)
        
        for p in soup.find_all("p"):
            try:
                rating = p["class"]
                if "star-rating" in rating:
                    review = rating[1]
            except KeyError:
                continue 

        return {"review_rating": review}


    def image(self, url):
        """
        Scrap the book cover
        """
        soup = self.get_soup(url)
        img_element = soup.img['src'].replace('../..', 'http://books.toscrape.com')
        img_data = requests.get(img_element)
        filename = 'data/image.jpg' #specify file name
        with open(filename, 'wb') as img_file:  #open binary file and write data
            img_file.write(img_data.content)

        return {
            'image_url': img_element,
        }
    
    def generate_data(self,url):
        """
        Save all the data scraped in a dict book_data
        """
        book_data = {}
        book_data.update(self.title(url))
        book_data.update(self.description(url))
        book_data.update(self.availability(url))
        book_data.update(self.reviews(url))
        book_data.update(self.category(url))
        book_data.update(self.prices(url))
        book_data.update(self.upc(url))
        book_data.update(self.image(url))

        return book_data