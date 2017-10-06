import sys
import os

import unittest
import math






def main():
    midpoint_test()    



def midpoint(f, a, b, n):
    h = float(b-a)/n
    midpoint = 0
    for i in range (n):
        midpoint += f((a + h/2.0) + i*h)
    return (midpoint*h)

def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    trap = (f(a)/2)+(f(b)/2)
    for i in range(n):
        trap += f(a+i*h)
    return (h*trap)

def simpsons2(f, a, b, n):
    h = float(b-a)/n
    simp = f(a)/6 + f(b)/6
    for i in range(1, n-1):
        simp += f(a+i*h)/3
    for i in range(1,n):
        simp+= 2*f(a+(i-(1/2))/h)/3
    return(h*simp)


def simpsons(f, a, b, n):
    h = float(b-a)/n
    k=0.0
    x=a+h
    for i in range(1,n/2+1):
        k +=4*f(x)
        x += 2*h
    x=a+2*h
    for i in range(1,n/2):
        k+=2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)




def midpoint_test():
    g = lambda x : x**2
    tester = MyTest(g)
    tester.test()



class MyTest(unittest.TestCase):
    def __init__(self, fx):
        self.g = fx
    def test(self):
        self.assertEqual(midpoint(self.g,0,8,4),168)
        self.assertEqual(trapezoidal(self.g,0,8,4),176)
        self.assertEqual(simpsons(self.g,0,8,4),170)




if __name__=="__main__":
    main()


