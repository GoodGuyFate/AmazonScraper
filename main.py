import requests
import bs4
import smtplib

# URL for the webpage you want to scrape
URL = "URL"

# User Agent headers, helps websites understand more about the device/os/browser/rendering engine
headers = {"User-Agent": ""}



def check_price():
    # Returns all data from webpage
    response = requests.get(URL, headers=headers)

    soup = bs4.BeautifulSoup(response.text, 'lxml')

    price_element = soup.select_one('span.a-price').select_one('span.a-price-whole')

    price_text = price_element.text.strip().replace(',', '')

    price_float = float(price_text)
    if price_float < 17000:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('EMAIL', 'PASSWORD')

    subject = "Price fell down!"
    body = "Check the amazon link: "

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'FROM',
        'TO',
        msg
    )
    print("EMAIL HAS BEEN SENT")
    server.quit()

check_price()