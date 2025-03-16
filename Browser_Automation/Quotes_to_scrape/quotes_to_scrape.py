from DrissionPage import ChromiumPage
from time import sleep
import csv, os, time

def open_browser():
    driver = ChromiumPage()
    return driver

def get_boxes(driver):
    boxes = driver.eles('xpath://div[@class="quote"]', timeout=10)
    return boxes

def extract_data(boxes):
    for box in boxes:
        description_tag = box.ele('xpath:./span[@class="text"]',timeout=0)
        description_text = description_tag.text if description_tag else ''
        author_tag = box.ele('xpath:.//small[@class="author"]',timeout=0)
        author_text = author_tag.text if author_tag else ''
        about_tag = box.ele('xpath:.//a[contains(@href,"/author/")]',timeout=0)
        about_url = about_tag.attr('href') if about_tag else ''
        qoutes_tags = box.eles('xpath:.//div[@class="tags"]//a',timeout=0)
        qoutes = [tag.text.strip() for tag in qoutes_tags]
        row = [description_text, author_text, about_url, qoutes]
        print('Saving Data:- ',row)
        save_data(row)

def save_data(row):
    with open('quotes_data.csv','a',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def csv_header():
    header = ['Quote','Author','About-URL','Tags']
    with open('quotes_data.csv','w',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)

def main():
    save_data_file = 'quotes_data.csv'
    if save_data_file not in os.listdir():
        csv_header()
    driver = open_browser()
    page = 1
    while True:
        website_url = f'https://quotes.toscrape.com/page/{page}/'
        print('Getting Page:- ',website_url)
        driver.get(website_url)
        sleep(2)
        boxes = get_boxes(driver)
        if not boxes:
            print('All Pages Scraped')
            break
        extract_data(boxes)
        page += 1

main()