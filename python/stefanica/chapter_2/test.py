import os
import sys
import math
from enum import Enum
from scipy.integrate import quad


f  = lambda x : 0.045 + (0.005*(1+x)*math.log(1+x))/x

#auxillary zero rate curve function


class pmt(Enum):
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
        self.price=-1


        print( self.__dict__)
    def calculate_v_cash_flows(self):
        for i in range(0,(j-h))
            self.v_cash_flow.append((self.c/self.p)*self.f)
        self.v_cash_flow.append(self.f+(self.c/2*self.f))
        print self.v_cash_flow
        return

    
 


def bond_yield(bond):
    if bond.price=-1:
        return 
    x_0 = 0.1 #initial guess 10%
    x_new = x_0
    x_old = x_0 -1.0
    tol = float(10**(-6))

    while(math.fabs(x_new - x_old) > tol):
        x_old = x_new

        numerator =
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
            price += (bond.f+(bond.c/2)*bond.f)*bond.discount_factor(inter[0], inter[1])
            break
        discount =bond.discount_factor(inter[0],inter[1])
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
    b = bond(100, 0.05, 2, 4, True, fx, pmts.SEMI_ANNUAL)
    b.bond_price_instant()
    print(b.price)






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
