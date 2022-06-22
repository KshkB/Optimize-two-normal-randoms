from getstats import returnStatistics
from optimalsolnHold import optimalHoldings
from timepartition import date_diff

import os

def optimizeInvestment(stock_X, stock_Y, start, end, investment):
    time_range_length = date_diff(start, end)

    print("Enter the number time periods to analyze:")
    intv = int(input().strip())

    l = time_range_length/intv

    stats = returnStatistics(stock_X, stock_Y, start, end, intv)

    meanX = stats[0]
    devX = stats[1]
    meanY = stats[2]
    devY = stats[3]
    corrXY = stats[4]

    price_X_start = stats[5]
    price_Y_start = stats[6]

    meanX_annualized = round(100 * meanX * (365/l), 2)
    devX_annualized = round(100 * devX * (365/l), 4)

    meanY_annualized = round(100*meanY*(365/l), 2)
    devY_annualized = round(100*devY*(365/l), 4)

    print(f"From the historical data:\n{stock_X} has an annualized growth of {meanX_annualized} percent with deviation {devX_annualized};\n{stock_Y} has an average annualized growth of {meanY_annualized} percent with deviation {devY_annualized}.")
    print(f"\nEnter your risk tolerace in the growth rate for the portfolio comprised of {stock_X} and {stock_Y}:\n")
    risk = float(input().strip())
    risk = risk/(100*365)
    os.system('clear')

    return optimalHoldings(meanX,devX, meanY, devY, corrXY, risk, investment, price_X_start, price_Y_start, l)


if __name__ == '__main__':
    os.system('clear')
    print('Enter the ticker codes of the two stocks to be optimized:')
    stock_X = str(input().strip())
    stock_Y = str(input().strip())

    os.system('clear')
    print("Enter the dates over which to optmize.")
    print('Starting year:')
    start_yr = str(input().strip())

    print('Starting month:')
    start_mth = str(input().strip())
    if len(start_mth) == 1:
        start_mth = '0'+start_mth
    
    print('Starting day:')
    start_day = str(input().strip())
    if len(start_day) == 1:
        start_day = '0'+start_day

    start = start_yr+start_mth+start_day

    print('Ending year:')
    end_yr = str(input().strip())

    print('Ending month:')
    end_mth = str(input().strip())
    if len(end_mth) == 1:
        end_mth = '0'+end_mth

    print('Ending day:')
    end_day = str(input().strip())
    if len(end_day) == 1:
        end_day = '0'+end_day

    end = end_yr + end_mth + end_day

    os.system('clear')
    print(f'Enter the desired amount to invest into holding {stock_X} and {stock_Y}')
    invest = float(input().strip())

    os.system('clear')
    hold_X, price_X, hold_Y, price_Y = optimizeInvestment(stock_X, stock_Y, start, end, invest)

    print(f"With an investment amount of {invest}:\nhold {hold_X} units of {stock_X} at {price_X} per share;\nhold {hold_Y} units of {stock_Y} at {price_Y} per share.")

