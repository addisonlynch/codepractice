import os
import sys
import math

from scipy.integrate import quad


def integrate_definite(f, a, b):
    return quad(f, a, b)[0]




#auxillary zero rate curve function
def rate_curve(x):
    strin = str(x)
    return{
        '0.5':0.05,
        '1.0':0.0525,
        '1.5':0.0535,
        '2.0':0.055
    }[strin]




def bond_price_instant(f,c,n):


#calculate the price of a semi-annual coupon bond given zero rate curve
def bond_price_sa(f, c, n):

    #compute the discount factor
    price =0
    def stepUp(i, j, s):
        while i<j:
            yield i
            i += s

    for i in stepUp(0.5,2,0.5):
        price += (c/2)*(f*math.exp((-1)*rate_curve(i)*i))
    price+=(f+(c/2)*f)*(math.exp((-1)*rate_curve(2.0)*(2.0)))
    return price




def main():
    p =bond_price_sa(100, 0.05, 4)
    print(p)

if __name__ == "__main__":
    main()
