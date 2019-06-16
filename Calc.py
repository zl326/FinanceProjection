# Contains mathematical functions

import math

# Monthly payment calculator, similar to PMT function in Excel.
# Takes annual interest rate as argument, not monthly rate
def PMT(presentValue, interestRate, nMonths):
  r = interestRate / 12
  payment = presentValue * r*(1+r)**nMonths / ((1+r)**nMonths - 1)
  return round(payment, 2)


def getMonthlyInterest(balance, interestRate):
  return round(balance * interestRate / 12, 2)