# getsymbols
Get financial stock data from Yahoo Finance.
This is a fixed version of pandas_datareader, using fix_yahoo_finance as an override.

It produces comma separated files for each ticker you provide.
Provide start date and ticker(s).
End date is optional, and it uses todays date if not provided.

Example of use:
Usage:
```javascript
$ python3 getsymbols.py --start=2012-01-01 --end=2017-12-31 --ticker=AAPL,INTC,TEL.OL,VEI.OL,NVDA
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
