import os
import sys
import math
from enum import Enum
from scipy.integrate import quad


f  = lambda x : 0.045 + (0.005*(1+x)*math.log(1+x))/x
#auxillary zero rate curve function

class pmts(Enum):
    ANNUAL = 1
    SEMI_ANNUAL = 2
    QUARTERLY = 3
    MONTHLY = 12
    WEEKLY = 52
    DAILY = 365

def calculateIntervals(length,n_intervals):
    intervals=[]
    h = float(length)/n_intervals
    htemp = h        
    while htemp <= length:
        intervals.append((float(htemp-h),float(htemp)))
        htemp += h
    return intervals

#face value, coupon rate, duration, number of intervals, discrete interest rates (bool), function, bond type
class bond(object):
    def __init__(self, face_value, coupon, duration, intervals, discr, func, pmts):
        self.f = face_value
        self.c = coupon
        self.j = duration
        self.n = intervals
        self.d = discr
        self.fx = func
        self.p = pmts
        self.h=float(duration)/intervals
        self.interval_list = calculateIntervals(self.j, self.n)
        self.t_cash_flow = [interval[1] for interval in self.interval_list]
        self.v_cash_flow = []
        self.calculate_v_cash_flows()
        self.price = float(100+(1/32))

    def set_price(self, price, auto=False):
        if auto:
            self.price = bond_price_stefanica(self)
        else:
            self.price = price



#        print( self.__dict__)

    def calculate_v_cash_flows(self):
        i = self.h
        while i <= (self.j-self.h):
            self.v_cash_flow.append((self.c/self.p)*self.f)
            i = i + self.h
        self.v_cash_flow.append(self.f+(self.c/2*self.f))
        print ([flow for flow in self.v_cash_flow])
        return

    def interest_rate(self,time):
        if self.d:
            return(self.fx[str(time)])
        else:
            return(quad(self.fx,0,time)[0])

    #requires: number of intervals(n), time of cash flows, value of cash flows
def bond_price_stefanica(bond):
    B = 0
    disc={}
    for i in range(0,bond.n):
        disc[i] = math.exp((-1)*bond.t_cash_flow[i]*bond.interest_rate(bond.t_cash_flow[i]))
        print("time " + str(bond.t_cash_flow[i]) + ": discount: " + str(disc[i]) + " | cf: " + str(bond.v_cash_flow[i]))

        B = B + bond.v_cash_flow[i] * disc[i]
    print(B)
    return

#From table 8.6
def bond_yield_stefanica(bond):
    if bond.price== (-1):
        return 
    x_0 = 0.1 #initial guess 10%
    x_new = x_0
    x_old = x_0 -1.0
    tol = float(10**(-6))

    while(math.fabs(x_new - x_old) > tol):
        print("x_new: " + str(x_new))
        x_old = x_new
        numerator =0 
        denominator = 0
        for i in range(0,bond.n):
            numerator += (bond.v_cash_flow[i]*math.exp(((-1)*x_old)*bond.t_cash_flow[i]))
        for j in range(0,bond.n):
            denominator += (bond.t_cash_flow[j]*bond.v_cash_flow[j]*math.exp(((-1)*x_old)*bond.t_cash_flow[j]))
        x_new = x_old + (float((numerator-bond.price))/denominator)
    return x_new

        
def discount_factor(bond,start,end):
        if bond.d:
            ans = bond.fx[str(end)]
        else:
            ans = quad(bond.fx,start,end)[0]        
        retval=math.exp((-1)*ans*(end))
        print("Discount factor for " + str(start)+ " to " + str(end)+ ": " + str(retval))
        return(retval)
  
def bond_price_instant(bond):
    price = float(0)
    for inter in bond.interval_list:
        if inter[1] == bond.j:
            price += (bond.f+(bond.c/2)*bond.f)*discount_factor(bond, inter[0], inter[1])
            break
        discount =discount_factor(bond,inter[0],inter[1])
        price += (bond.c/2)*bond.f*discount
    bond.price = price
    print(price)
    print("Price set.")
    return

def main():
    fx ={
        '0.5':0.05,
        '1.0':0.0525,
        '1.5':0.0535,
        '2.0':0.055
    }
    b = bond(100, 0.03375, 2, 4, True, fx, 2)



    c = bond(100, 0.08, 2, 6, True, fx, 2)
    print(bond_yield_stefanica(c))


'''
def rate_curve(x):
    strin = str(x)
    return{
        '0.5':0.05,
        '1.0':0.0525,
        '1.5':0.0535,
        '2.0':0.055
    }[strin]

'''





    

#calculate the price of a semi-annual coupon bond given zero rate curve


if __name__ == "__main__":
    main()
