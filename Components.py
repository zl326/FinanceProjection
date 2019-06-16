# Class definitions

import Calc

# Any kind of capital repayment loan, 
# e.g. mortgage
#
# interest as a decimal
# termLength in months
class Loan:
  def __init__(self, name, balance, interestRate, termRemaining):
    self.name = name
    self.balance = balance
    self.interestRate = interestRate
    self.termCurrent = 1
    self.termRemaining = termRemaining-1

    self.calculateRepayment()
    self.calculateInterest()

  def setBalance(self, newBalance):
    self.balance = newBalance

  def offsetBalance(self, deltaBalance):
    self.balance = round(self.balance + deltaBalance, 2)

  def calculateRepayment(self):
    self.repayment = Calc.PMT(self.balance, self.interestRate, self.termRemaining+1)

  def setRepayment(self, newRepayment):
    self.repayment = round(newRepayment, 2)

  def performTransactions(self):
    self.offsetBalance(self.interest - self.repayment)

  def setInterestRate(self, newInterestRate):
    self.interestRate = newInterestRate

  def calculateInterest(self):
    self.interest = Calc.getMonthlyInterest(self.balance, self.interestRate)

  def incrementTermCurrent(self):
    self.termCurrent += 1
    self.termRemaining -= 1






