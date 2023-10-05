import csv


def write_csv(books_dict):
    """
    Write all the data into file.csv
    
    :args --> books_dict is a list of dicts contain all the data needed
    """
    #define columns names
    csv_columns = ['product_page_url',
                  'universal_product_code(upc)',
                  'title',
                  'price_excluding_tax',
                  'price_including_tax',
                  'number_available',
                  'product_description',
                  'category',
                  'review_rating',
                  'image_url']
    
    #define csv_path to find file.csv
    csv_path = 'data/test.csv'

    #Open the file and write down all the data into the attributed columns
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer.writeheader()
        for data in books_dict:
            writer.writerow(data)