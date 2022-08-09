# Web-Scraping
We are web scraping stock price from yahoo finace.

## Steps For Webscraping Custom Stock Price
### Getting the Url
*  Goto Yahoo Finance and 
*  Search for your Stock 
*  Copy that Url
*  Use That in the Program

### Executing program

* install all the packages
* download the stock_price.py and keep it in your work folder
* Import it and work with it
* example 
```
import stock_price
url = "Your Custom Stock Price Url"
stock = stock_price.StockPrice()
stock.connect(url)
```


## Installing
Using pip
```
pip install beautifulsoup4
pip install requests
```


