from bs4 import BeautifulSoup
import requests
from lxml import html
import os


class Book:
    """
    A class for scraping book data from a specific URL.
    """

    def get_soup(self, url):
        """
        Fetches and returns BeautifulSoup object for a given URL.
        Args:
            url (str): The URL of the web page to scrape.
        Returns:
            soup: A BeautifulSoup object representing the parsed HTML content.
        """
        html = requests.get(url).content.decode("utf8").encode("utf8", "ignore")
        soup = BeautifulSoup(html, "lxml")
        return soup

    def get_url(self, url):
        """
        Extracts and returns the product page URL.
        Args:
            url (str): The URL of the product page.
        Returns:
            dict: A dictionary containing the product page URL.
        """
        return {"product_page_url": url}

    def get_title(self, url):
        """
        Extracts and returns the title of the book from the soup object.
        Args:
            soup (BeautifulSoup): The BeautifulSoup object representing the parsed HTML content.
        Returns:
            dict: A dictionary containing the book title.
        """
        soup = self.get_soup(url)
        return {"title": soup.h1.text}

    def get_reviews(self, url):
        """
        Extracts and returns review rating and product description from the soup object.
        Args:
            soup (BeautifulSoup): The BeautifulSoup object representing the parsed HTML content.
        Returns:
            dict: A dictionary containing review rating and product description.
        """
        soup = self.get_soup(url)
        desc = ""
        review = ""

        for i in soup.find_all("p"):
            try:
                star = i["class"]
                if "star-rating" in star:
                    review = star[1]
            except KeyError:
                desc = i.text
        return {"review_rating": review, "product_description": desc}

    def get_category(self, url):
        """
        Extracts and returns the category of the book from the soup object.

        Args:
            soup (BeautifulSoup): The BeautifulSoup object representing the parsed HTML content.

        Returns:
            dict: A dictionary containing the book category.
        """
        soup = self.get_soup(url)
        for a in soup.ul.find_all("a"):
            if "Home" not in a.text and "Books" not in a.text:
                return {"category": a.text}

    def get_upc_prices(self, url):
        """
        Extracts and returns UPC, prices, and availability from the soup object.
        Args:
            soup (BeautifulSoup): The BeautifulSoup object representing the parsed HTML content.
        Returns:
            dict: A dictionary containing UPC, prices, and availability.
        """
        soup = self.get_soup(url)

        upc = ""
        excluding_tax = ""
        including_tax = ""
        availability = ""

        for tr in soup.find_all("tr"):
            if "UPC" in tr.text:
                upc = tr.td.text
            elif "excl" in tr.text:
                excluding_tax = tr.td.text.replace("Â", "")
            elif "incl" in tr.text:
                including_tax = tr.td.text.replace("Â", "")
            elif "Availability" in tr.text:
                availability = (
                    tr.td.text.split(" ")[3].replace("(", "").replace(")", "")
                )
        return {
            "universal_product_code(upc)": upc,
            "price_excluding_tax": excluding_tax,
            "price_including_tax": including_tax,
            "availablility": availability,
        }

    def get_img(self, url):
        """
        Downloads the book cover image and returns image URL and local path.
        Args:
            soup (BeautifulSoup): The BeautifulSoup object representing the parsed HTML content.
            url (str): The URL of the book page.
            category (str): The category of the book.
            title (str): The title of the book.
        Returns:
            dict: A dictionary containing image URL and local path.
        """
        soup = self.get_soup(url)

        img_url = soup.img["src"].replace("../..", "http://books.toscrape.com")
        img = requests.get(img_url)
        category = self.get_category(url)
        title = self.get_title(url)
        path = "data/" + category["category"] + "/imgs"
        img_title = "".join([x for x in title["title"] if x.isalnum()]) + ".jpg"

        if not os.path.exists(path):
            os.makedirs(path)
        # write image
        open(path + "/" + img_title, "wb").write(img.content)

        return {"image_url": img_url, "image_path": path + "/" + img_title}

    def generate_data(self, url):
        """
        Scrapes and returns data for a book from the given URL.
        Args:
            url (str): The URL of the book page.
        Returns:
            dict: A dictionary containing book data.
        """
        book_data = {}
        book_data.update(self.get_url(url))
        book_data.update(self.get_title(url))
        book_data.update(self.get_reviews(url))
        book_data.update(self.get_category(url))
        book_data.update(self.get_upc_prices(url))
        book_data.update(self.get_img(url))

        return book_data
