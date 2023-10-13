import requests
from bs4 import BeautifulSoup
from book import Book
from csv_books import write_csv

"""
File: main.py

This file contains functions using to scrap book data into a csv files and extract images book.
Run the project by the bash command : python main.py.
"""


def get_categories():
    """
    Retrieves and returns the URLs of all book categories from the website.
    Returns:
        dict: A dictionary containing category names as keys and their corresponding URLs as values.
    """
    html = requests.get("http://books.toscrape.com/index.html")
    soup = BeautifulSoup(html.text, "lxml")

    categories = {}
    for i in soup.find("div", {"class": "side_categories"}).ul.find_all("a"):
        if "books_1" not in i.get("href"):
            categories[
                i.text.replace("\n", "").replace("  ", "")
            ] = "http://books.toscrape.com/" + i.get("href")
    return categories


def get_books_url(cat_url, nb_pages):
    """
    Retrieves and returns the URLs of books from a specific category.
    Args:
        cat_url (str): The URL of the category.
        nb_pages (int): The number of pages in the category.
    Returns:
        list: A list of book URLs.
    """
    books_url = []
    for i in range(nb_pages):
        html = requests.get(cat_url)
        soup = BeautifulSoup(html.text, "lxml")

        for book in soup.find_all("article"):
            book_url = book.h3.a.get("href").replace(
                "../../../", "http://books.toscrape.com/catalogue/"
            )
            books_url.append(book_url)

        if nb_pages > 1:
            nextPage = requests.get(
                cat_url.replace("index.html", "page-" + str(i + 2) + ".html")
            )
            soup = BeautifulSoup(nextPage.text, "lxml")

    return books_url


def scrape_books_from_category(cat_url):
    """
    Scrapes book data from a specific category.
    Args:
        cat_url (str): The URL of the category.
    Returns:
        list: A list of dictionaries containing book data.
    """
    html = requests.get(cat_url)
    soup = BeautifulSoup(html.text, "lxml")

    if soup.find("ul", {"class": "pager"}):
        nb_pages = int(
            soup.find("li", {"class": "current"}).text.split(" ")[31].replace("\n", "")
        )
    else:
        nb_pages = 1

    books_url = get_books_url(cat_url, nb_pages)

    all_books = []
    for url in books_url:
        current_book = Book().generate_data(url)
        all_books.append(current_book)

    return all_books


def main():
    """
    Main function to initiate the scraping process and write data to CSV files.
    """
    categories = get_categories()
    print("Scrapping in progress...")

    for categorie, cat_url in categories.items():
        all_books = scrape_books_from_category(cat_url)
        write_csv(all_books)
        print(
            "Successfully scrapped "
            + str(len(all_books))
            + " books from "
            + categorie
            + " category"
        )


if __name__ == "__main__":
    main()
