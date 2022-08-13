""" This program will take inputs for principal, rate of interst and time period in year to calculate EMI"""
import sys
#INPUT
#import math
#taking inout for principal amount
#initiation of variable

P=R=N=1
try:
	P=(float(sys.argv[1])*100000)
except:
	print("the value is not defin ")

#taking input for rate of interest in months
try:
	R=float(sys.argv[2])
except:
	print("Something wrong")
#omething
try:
	N=float(sys.argv[3])
except:
	print("something wrong")

#LOGIC
#lOGIC 1 : conervsion of yearly interst rate into monthly rate
r=R/12/100

#LOGIC2
EMI=((P*r)*((1+r)**N))/((1+r)**(N-1))
#EMI=((P*R*)(1+R)**N))/((1+R)(**N)-1)
#OUTPUT
print (EMI)