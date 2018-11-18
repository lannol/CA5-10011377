# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:06:30 2018

@author: Olivia
"""

import math
from functools import reduce


#lambda
add = lambda x,y: x+y

subtract = lambda x,y: x-y
    
divide = lambda x,y: x/y
        
multiply= lambda x,y: x*y

square = lambda x: x*x

exponent = lambda x,y: x**y
        
sqrt = lambda x: math.sqrt(x)


n = [1, 2, 5, 25]
m = [2, 2, 6, 8]

print(list(map(lambda x: x*x, n)))
print(list(map(square, n))) #this code gives the same result as the first line above but easier to use
print(list(map(add, n,m)))
print(list(map(divide, n,m)))
print([x**2 for x in n]) #same as square in the first line

print(list(filter(lambda x:x>=5, n)))
print(list(filter(lambda x:x<6, m)))

print(reduce(multiply, n))
print(reduce(multiply, m))
print(reduce(divide, n))


#list comprehensions
under_10= [x for x in range (10)] 
square2 = [x*x for x in under_10]
print(square2)

add2 = [x+x for x in under_10]
print(add2)

#generator
nums = (x*x for x in [1,2,3,4,5]) #square
print(nums)
for num in nums:
    print(num)


nums = (x+x for x in [2,4,6]) #adding
print(nums)
for num in nums:
    print(num)


nums = (x+x for x in [2,4,6]) #converting the add generator to list
print(list(nums))
