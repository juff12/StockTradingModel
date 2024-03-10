from polygon import RESTClient
import pandas as pd
from pathlib import Path
import pickle
from datetime import date
import tqdm

def get_ticker_data(presets: tuple, client: RESTClient):
    ticker, multiplier, timespan, start, end, limit = presets
    aggs = []
    _ticker = "X:" + ticker #format the ticker
    for a in client.list_aggs(ticker=_ticker, multiplier=multiplier, 
                              timespan=timespan, from_=start, to=end, limit=limit):
        aggs.append(a)

    df = pd.DataFrame(aggs)
    filestring = 'data/crypto/data/raw/{t}/{t}_{m}_{b}_data_raw.csv'.format(t=str(ticker).lower(),
                                                                            m=str(multiplier),
                                                                            b=timespan)
    filepath = Path(filestring)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath)

# code of scipt
def main():
    # read in the iterables
    coinbase_tickers = pickle.load(open('data/crypto/iterables/coinbase_tickers.pkl', 'rb'))
    time_intervals = pickle.load(open('data/crypto/iterables/time_intervals.pkl', 'rb'))
    
    # yapi key
    api_key = ""

    # connect to API
    client = RESTClient(api_key=api_key)

    # presets
    start = '2018-01-01'
    end = date.today().strftime('%Y-%m-%d')
    limit = 50000

    # # daily data
    for ticker in tqdm(coinbase_tickers):
        for bartime in time_intervals:
            multiplier, timespan = bartime.split('_')
            # reformats minute
            if timespan == 'minute':
                timespan = 'minute'
                start = '2020-01-01'
            presets = (ticker,int(multiplier),timespan,start,end,limit)
            get_ticker_data(presets, client)

# run scripts
if __name__ == '__main__':
    main()