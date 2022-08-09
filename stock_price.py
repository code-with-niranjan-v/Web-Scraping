import requests
from bs4 import BeautifulSoup


class StockPrice:
    def __init__(self):
        self.google_url = "https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch"
        self.apple_url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
        self.tesla_url = "https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch"
        self.choice()

    def choice(self):
        print("Select Stock Price")
        option = int(input("1.Google\n2.Apple\n3.Tesla\n4.Custom\nEnter the Choice: "))
        if option == 1:
            self.connect(self.google_url)

        elif option == 2:
            self.connect(self.apple_url)

        elif option == 3:
            self.connect(self.tesla_url)

        elif option == 4:
            self.custom()

        else:
            print("Invalid Choice!!")

    def connect(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        s = soup.find('div', id="app")
        s = s.find('fin-streamer', class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")
        print(s.text)
        return s.text

    def custom(self):
        print("Select The Url from Yahoo Finance For the Program To Work")
        url = input("Enter The url: ")
        self.connect(url)
