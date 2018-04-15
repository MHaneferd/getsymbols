# Small yahoo finance getter script
# Version 1.0
# 15. april 2018
# By Martin Haneferd
#
# For retrieving stock prices from yahoo finance:
#
# mac$ python3 getsymbols.py --help
# usage: getsymbols.py [-h] -s START [-e END] -t TICKER
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -s START, --start START
#                         The Start Date - format YYYY-MM-DD
#   -e END, --end END     The End Date - format YYYY-MM-DD (If not used, todays
#                         date will be)
#   -t TICKER, --ticker TICKER
#                         Ticker list - example: AAPL,INTC,TEL.OL

from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import argparse
import datetime


def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

if __name__ == "__main__":

    yf.pdr_override() # Very important

    parser = argparse.ArgumentParser()

    parser.add_argument('-s','--start', help="The Start Date - format YYYY-MM-DD ", required=True, type= valid_date)
    parser.add_argument('-e','--end',  help="The End Date - format YYYY-MM-DD (If not used, todays date will be) ", required=False,type = valid_date)
    parser.add_argument('-t','--ticker', type=str, help="Ticker list - example: AAPL,INTC,TEL.OL", required=True)
    args = parser.parse_args()

    ticker_list = args.ticker.split(',')  # ['AAPL','INTC','TEL.OL']
    start = args.start
    end = args.end
    if end == None: # If end date is empty, use today.
        end = datetime.datetime.today()

    for ticker in ticker_list:

        # Get ticker data
        data = pdr.get_data_yahoo(ticker, start=start, end= end)

        # Save result in a csv file, named ticker.csv
        file = "./" + ticker + ".csv"
        data.to_csv(file)
