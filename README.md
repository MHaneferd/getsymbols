# getsymbols
Get financial stock data from Yahoo Finance.
This is a fixed version of pandas_datareader, using fix_yahoo_finance as an override.

It produces comma separated files for each ticker you provide.

Example of use:
Usage:
```javascript
$ python3 getsymbols.py -s=2012-01-01 -t=AAPL,INTC,TEL.OL,VEI.OL,NVDA
```

For help menu:

```javascript
$ python3 getsymbols.py -h

usage: getsymbols.py [-h] -s START [-e END] -t TICKER

optional arguments:
  -h, --help            show this help message and exit
  -s START, --start START
                        The Start Date - format YYYY-MM-DD
  -e END, --end END     The End Date - format YYYY-MM-DD (If not used, todays
                        date will be)
  -t TICKER, --ticker TICKER
                        Ticker list - example: AAPL,INTC,TEL.OL
```
