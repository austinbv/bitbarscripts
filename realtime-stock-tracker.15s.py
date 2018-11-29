#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# <bitbar.title>Stock Tracker</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Austin Vance</bitbar.author>
# <bitbar.author.github>austinbv</bitbar.author.github>
# <bitbar.desc>Show a rotating list live stock prices in your menu bar</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

import json, urllib2, sys

def get_stock_price(stock):
    try:
        response = urllib2.urlopen('https://api.iextrading.com/1.0/stock/' + stock + '/quote')
        return json.loads(response.read())
    except:
        print "Loading"
        sys.exit(1)

def create_output_string(stock, response):
    output = {'stock': stock}
    output['deliminitor'] = "▲" if response["changePercent"] > 0 else "▼"
    output['price'] = "{:0.2f}".format(response["latestPrice"])
    output['percent_change'] = "{:0.2f}".format(response["changePercent"] * 100.00)
    output['color'] = "red" if response["changePercent"] < 0 else "green"

    return "{stock} {deliminitor} ${price} ({percent_change}) | color = {color}".format(**output)

def main():
    stocks = ["PVTL", "PYPL", "GOOS"]

    for stock in stocks:
        response = get_stock_price(stock)
        print create_output_string(stock, response)

if __name__ == "__main__":
    main()
