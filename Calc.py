# Contains mathematical functions

import math

# Monthly payment calculator, similar to PMT function in Excel.
# Takes annual interest rate as argument, not monthly rate
def PMT(presentValue, interestRate, nMonths):
  r = interestRate / 12
  payment = presentValue * r*(1+r)**nMonths / ((1+r)**nMonths - 1)
  return floor(payment)


def getMonthlyInterest(balance, interestRate):
  return floor(balance * interestRate / 12)

# Floor number to 2 decimal places
def floor(value):
  dp = 2 # Number of decimal places
  return math.floor(value * 10.0**dp) / 10.0**dp