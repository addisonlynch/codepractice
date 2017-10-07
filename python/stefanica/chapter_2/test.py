import os
import sys
import math

from scipy.integrate import quad


f  = lambda x : 0.045 + (0.005*(1+x)*math.log(1+x))/x

#auxillary zero rate curve function


def calculateIntervals(length,n_intervals):
    intervals=[]
    h = float(length)/n_intervals
    htemp = h        
    while htemp <= length:
        intervals.append((float(htemp-h),float(htemp)))
        htemp += h
    return intervals


class bond(object):
    def __init__(self, face_value, coupon, duration, intervals, discr, func):
        self.f = face_value
        self.c = coupon
        self.j = duration
        self.n = intervals
        self.d = discr
        self.fx = func
        self.h=float(duration)/intervals
        self.interval_list = calculateIntervals(self.j, self.n)

        print( self.__dict__)
    
    def discount_factor(self,start,end):
        if self.d:
            ans = self.fx[str(end)]
        else:
            ans = quad(self.fx,start,end)[0]        
        retval=math.exp((-1)*ans*(end))
        print("Discount factor for " + str(start)+ " to " + str(end)+ ": " + str(retval))
        return(retval)
      
    def bond_price_instant(self):
        price = float(0)
        for inter in self.interval_list:
            if inter[1] == self.j:
                price += (self.f+(self.c/2)*self.f)*self.discount_factor(inter[0], inter[1])
                break
            discount =self.discount_factor(inter[0],inter[1])
            price += (self.c/2)*self.f*discount
        self.price = price
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
    b = bond(100, 0.05, 2, 4, True, fx)
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
