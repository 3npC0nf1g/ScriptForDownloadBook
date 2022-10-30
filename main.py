from bs4 import BeautifulSoup
import requests

html_page = requests.get("https://www.adminbox.eu/fr/inbox?called_from_inbox_filter=true&doc_type=&from=01%2F08%2F2021&page=1&sender=&to=01%2F09%2F2021")

soup = BeautifulSoup(html_page.content)

pdf_links = [link for link in soup.findAll('a') if str(link.get("href")).endswith(".pdf")]

for pdf_link in pdf_links:

    pdf_name = pdf_link.get("href")[pdf_link.get("href").rfind("/") + 1: len(pdf_link.get("href"))]

    with open(pdf_name, "wb") as pdf:
        pdf.write(requests.get(pdf_link.get("href")).content)

    print("i finish download "+pdf_name)

print("I finish all")