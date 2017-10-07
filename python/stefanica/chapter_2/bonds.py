import os
import sys
import math

from scipy.integrate import quad


def integrate_definite(f, a, b):
    return quad(f, a, b)[0]


f  = lambda x : 0.045 + (0.005*(1+x)*math.log(1+x))/x


#auxillary zero rate curve function
def rate_curve(x):
    strin = str(x)
    return{
        '0.5':0.05,
        '1.0':0.0525,
        '1.5':0.0535,
        '2.0':0.055
    }[strin]



#function,face_value coupon, duration, intervals, discreet
def bond_price_instant(f,c,j,n,d,fx):
    h=j/n

    def calculateIntervals(length,n_intervals):
        intervals=[]
        h = float(length)/n_intervals
        htemp = h
        while htemp <= length:
            intervals.append((float(htemp-h),float(htemp)))
            htemp += h
        return intervals

    interval_list = calculateIntervals(j,n)
    #print(calculateIntervals(2,4)[0][0])
    
    def stepUp(i,j,s):
        while i<j:
            yield i
            i += s

    def discount_factor(start,end,discr,fx):
        if discr:
            ans = rate_curve(end)
        else:
            ans =quad(fx,start,end)[0]        
        retval= math.exp((-1)*ans*(end))
        print("Discount factor for " + str(start)+ " to " + str(end)+ ": " + str(retval))
        return retval
    price = float(0)
    for inter in interval_list:
        if inter[0] == j-h:
            price += (f+(c/2)*f)*discount_factor(inter[0], inter[1],d,fx)
            break
        discount =discount_factor(inter[0],inter[1],d,fx)
        price += (c/2)*f*discount
    
   
    return price
    

#calculate the price of a semi-annual coupon bond given zero rate curve


def main():

    p =bond_price_instant(100, 0.05, 2, 4, True, "None")
    print(p)

if __name__ == "__main__":
    main()
