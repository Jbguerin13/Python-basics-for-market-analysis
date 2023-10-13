import csv

"""
file: csv_writer.py
This file contains function for writing all the scraped book data into CSV files.
"""


def write_csv(books):
    """
    Writes the book data to a CSV file for a specific category.
    Args:
        books (list): A list of dictionaries containing book data.
    Returns:
        None
    """
    csv_columns = [
        "title",
        "universal_product_code(upc)",
        "product_page_url",
        "price_excluding_tax",
        "price_including_tax",
        "availablility",
        "product_description",
        "category",
        "review_rating",
        "image_url",
        "image_path",
    ]
    categorie = books[0]["category"]
    csv_file = categorie + ".csv"

    with open("data/" + categorie + "/" + csv_file, "w", errors="replace") as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
        writer.writeheader()
        for data in books:
            writer.writerow(data)
