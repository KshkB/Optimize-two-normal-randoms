from math import sqrt, inf, floor, exp
import operator

## HELPER METHOD
## FROM A LIST OF OPTIMA FOR func, GET THAT OPTIMA THAT MAXIMIZES func
def getMaximum(optima, func):
    optima_vals = {opt: func(opt) for opt in optima}
    maxima = max(optima_vals.items(), key=operator.itemgetter(1))[0]
    return maxima

def getMaximum2(optima, func):
    curr_val = -inf
    maxima = {}
    for opt in optima:
        if func(opt) > curr_val:
            curr_val = func(opt)
            maxima['maxima'] = opt
        
    return maxima['maxima']

## MAX FOR STATS
def maxSoln(meanX, devX, meanY, devY, corrXY, risk):
    
    ## PARAMATERS ARE COEFFICIENTS lambda, delta
    def portfolioGrowth(param):
        lam = param[0]
        delta = param[1]
        return lam*meanX + delta*meanY

    denom_const = (devX**2) * (devY**2) - corrXY*corrXY
    numerator_const_1 = devX*((devY**2)*meanX - corrXY*meanY)
    numerator_const_2 = devY*((devX**2)*meanY - corrXY*meanX)

    const1 = numerator_const_1/denom_const
    const2 = numerator_const_2/denom_const
    const3 = (const1/devX) * (const2/devY) * corrXY

    opt_const = abs(sqrt(const1 + const2 + 2*const3))/risk

    lam_pos = (1/opt_const) * (numerator_const_1/devX)/denom_const
    lam_neg = (-1)*lam_pos
    del_pos = (1/opt_const) * (numerator_const_2/devY)/denom_const
    del_neg = (-1)*del_pos

    optima = [
        (lam_pos, del_pos), 
        (lam_pos, del_neg), 
        (lam_neg, del_pos),
        (lam_neg, del_neg)
        ]
    
    return getMaximum(optima, portfolioGrowth)

## RETURN OPTIMAL HOLDINGS FROM maxSoln RESULTS
def optimalHoldings(meanX, devX, meanY, devY, corrXY, risk, invest, priceX, priceY, l):
    maxima = maxSoln(meanX, devX, meanY, devY, corrXY, risk)
    lam = maxima[0]
    delta = maxima[1]
    if corrXY == 1 or corrXY == -1:
        return inf, inf

    ## TERMS
    a = exp(lam * meanX * l + delta * meanY * l) 
    b = exp(meanY * l)
    c = exp(meanX * l)

    holdingX = (1/priceX) * invest * (a - b)/(c - b)
    holdingX = floor(holdingX)

    holdingY = (1/priceY) * invest * (c - a)/(c - b)
    holdingY = floor(holdingY)

    return holdingX, priceX, holdingY, priceY


