#此為計算如何還清卡債的程式，利用bisection search求出每個月最少須還多少錢，以便在一年後還清
balance = 320000
#卡債
annualInterestRate = 0.2
#年利率
paybot = balance/12
#若年利率等於0，需還的金額(最低)
payup = balance*(1+annualInterestRate)**12
#若每月均不償還，至年底需一次還清的金額(最高)
midpay = (paybot+payup)/2

def pay(paybot,payup):
    midpay = (paybot+payup)/2    
    for month in range (11):
        Novbal = (balance - midpay)*(1 + annualInterestRate/12)
            
    for month in range (12):
        Decbal = (balance - midpay)*(1 + annualInterestRate/12)
    
    if Novbal <= 0:
        payup = midpay
        return pay(paybot,payup)
    elif Decbal > 0:
        paybot = midpay
        return pay(paybot,payup)
    else:
        return midpay
    
print ("Lowest Payment: "+str(round(pay(paybot,payup),2)))        