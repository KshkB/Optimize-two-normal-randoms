from secrets import IEX_CLOUD_API_TOKEN, IEX_CLOUD_SANDBOX
from iexfinance.stocks import get_historical_data
import timepartition
from math import log
from statistics import mean, stdev
from scipy.stats import pearsonr

## SANDBOX TESTING
import os
os.environ['IEX_API_VERSION'] = 'iexcloud-sandbox'

def returnStatistics(stock_X, stock_Y, start, end, intv):
    dates = timepartition.date_range(start, end, intv)
    dates = list(dates)

    growths_X = []
    growths_Y = []

    price_data_X = get_historical_data(stock_X, start, end, close_only=True, token=IEX_CLOUD_SANDBOX)
    price_data_Y = get_historical_data(stock_Y, start, end, close_only=True, token=IEX_CLOUD_SANDBOX)

    for i, d in enumerate(dates):
        if i < len(dates) - 1:
            start_i = d
            end_i = dates[i+1]

            start_price_X = timepartition.priceDateVerifyAdd(price_data_X, start_i)
            end_price_X = timepartition.priceDateVerifySub(price_data_X, end_i)

            start_price_Y = timepartition.priceDateVerifyAdd(price_data_Y, start_i)
            end_price_Y = timepartition.priceDateVerifySub(price_data_Y, end_i)

            growth_in_X = log(end_price_X/start_price_X) 
            growths_X.append(growth_in_X)

            growth_in_Y = log(end_price_Y/start_price_Y)
            growths_Y.append(growth_in_Y)

    mean_X = mean(growths_X)
    dev_X = stdev(growths_X)

    mean_Y = mean(growths_Y)
    dev_Y = stdev(growths_Y)
    
    pearson = pearsonr(growths_X, growths_Y)

    corr_XY = pearson[0] * dev_X * dev_Y

    price_X_at_start = timepartition.priceDateVerifyAdd(price_data_X, start)
    price_Y_at_start = timepartition.priceDateVerifyAdd(price_data_Y, start)

    return mean_X, dev_X, mean_Y, dev_Y, corr_XY, price_X_at_start, price_Y_at_start, growths_X


## TESTING
if __name__ == '__main__':

    stock_X = 'SPY'
    stock_Y = 'TSLA'

    start = '20150304'
    end = '20201012'

    intv = 10
    mnX = returnStatistics(stock_X, stock_Y, start, end, intv)[0]
    dvX = returnStatistics(stock_X, stock_Y, start, end, intv)[1]

    tot = timepartition.date_diff(start, end)
    #print(100*mnX*(365/(tot/intv)), 100*dvX*(365/(tot/intv)))

    print(returnStatistics(stock_X, stock_Y, start, end, intv)[-1])

