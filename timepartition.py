from datetime import datetime, timedelta
import os

## COMPUTE THE DIFFERENCE BETWEEN DATES IN DAYS
def date_diff(start, end):
    start = datetime.strptime(start,"%Y%m%d")
    end = datetime.strptime(end,"%Y%m%d")
    diff = end - start
    return diff.days

## ROUND TO THE NEAREST MONTH OR YEAR
def date_diffRound(start, end):
    days = date_diff(start, end)
    yrs = days/365

    year_ranges = [1, 2, 5]
    mth_ranges = [1, 3, 6]

    if yrs >=1:
        yr = year_ranges[0]
        for i in year_ranges:
            if yrs - i > 0:
                yr = i
        return str(yr)+'y'

    if yrs < 1:
        mth = mth_ranges[0]
        if yrs > 0.75:
            mth = year_ranges[0]
            return str(mth)+'y'
        if yrs <=0.75:     
            for i in mth_ranges:
                if yrs - i/12 > 0:
                    mth = i
            return str(mth)+'m'

## ROUND TO THE NEAREST YEAR
def date_diffRound2(start, end):
    days = date_diff(start, end)
    yrs = days/365
    if yrs >=1:
        yrs = days//365
        return str(yrs) + 'y'
    if yrs<1:
        return str(1)+'y'

## RETURN A LIST OF DATES SEPERATED INTO intv PERIODS
def date_range(start, end, intv):
    start = datetime.strptime(start,"%Y%m%d")
    end = datetime.strptime(end,"%Y%m%d")
    diff = (end  - start ) / intv
    for i in range(intv):
        yield (start + diff * i).strftime("%Y%m%d")
    yield end.strftime("%Y%m%d")

## IF NO DATA AT SPECIFIED DATE, GOTO NEXT DAY
def priceDateVerifyAdd(stockPrice_data, date):
    try:
        return stockPrice_data['close'][date]
    except KeyError:
        date = datetime.strptime(date, '%Y%m%d')
        date = date + timedelta(days=1)
        date = date.strftime('%Y%m%d')
        return priceDateVerifyAdd(stockPrice_data, date)

## IF NO DATA AT SPECIFIED DATE, GO TO PREVIOUS DAY
def priceDateVerifySub(stockPrice_data, date):
    try:
        return stockPrice_data['close'][date]
    except KeyError:
        date = datetime.strptime(date, '%Y%m%d')
        date = date - timedelta(days=1)
        date = date.strftime('%Y%m%d')
        return priceDateVerifySub(stockPrice_data, date) 

## TESTING
if __name__ == '__main__':
    os.system('clear')
    print(f"Enter the starting date (year/month/day):")
    yr_start = str(input().strip())
    mth_start = str(input().strip())
    if len(mth_start) == 1:
        mth_start = '0'+mth_start
    day_start = str(input().strip())
    if len(day_start) == 1:
        day_start = '0'+day_start

    start = yr_start+mth_start+day_start

    print(f"Enter the end date (year/month/day):")
    yr_end = str(input().strip())
    mth_end = str(input().strip())
    if len(mth_end) == 1:
        mth_end = '0'+mth_end
    day_end = str(input().strip())
    if len(day_end) == 1:
        day_end = '0'+day_end

    end = yr_end+mth_end+day_end

    print("Enter the period length (a positive integer):")
    intv = int(input().strip())

    dates = date_range(start, end, intv)
    dates = list(dates)
    print(dates)
