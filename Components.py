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
    self.termRemaining = termRemaining

    self.calculateRepayment()
    self.calculateInterest()

  def setBalance(self, newBalance):
    self.balance = newBalance

  def offsetBalance(self, deltaBalance):
    self.balance += deltaBalance

  def calculateRepayment(self):
    self.repayment = Calc.PMT(self.balance, self.interestRate, self.termRemaining)

  def setRepayment(self, newRepayment):
    self.repayment = newRepayment

  def setInterestRate(self, newInterestRate):
    self.interestRate = newInterestRate

  def calculateInterest(self):
    self.interest = Calc.getMonthlyInterest(self.balance, self.interestRate)

  def decrementTermRemaining(self):
    self.termRemaining -= 1






