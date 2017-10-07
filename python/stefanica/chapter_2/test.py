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
        self.h=self.j/self.n
        self.interval_list = calculateIntervals(self.j, self.n)

    #function,face_value coupon, duration, intervals, discreet
    def bond_price_instant(self):

        
        #print(calculateIntervals(2,4)[0][0])
        def discount_factor(start,end):
            if self.discr:
                return self.fx(str(end))
            else:
                return math.exp((-1)*quad(self.fx,start,end)[0]*(end))        
     #       retval= ans
    #        print("Discount factor for " + str(start)+ " to " + str(end)+ ": " + str(retval))
        price = float(0)
        for inter in self.interval_list:
            if inter[1] == self.j:
                price += (f+(c/2)*f)*discount_factor(inter[0], inter[1])
                break
            discount =discount_factor(inter[0],inter[1])
            price += (c/2)*f*discount
        self.price = price
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