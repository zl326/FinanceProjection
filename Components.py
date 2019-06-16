# Class definitions

import Calc

# Any kind of capital repayment loan, 
# e.g. mortgage
#
# interest as a decimal
# termLength in months
class Loan:
  def __init__(self, name, balance, interestRate, termCurrent, termRemaining):
    self.name = name
    self.balance = balance
    self.interestRate = interestRate
    self.termCurrent = termCurrent
    self.termRemaining = termRemaining-1

    self.repaymentVoluntary = 0
    self.repaymentPenalty = 0
    self.repaymentCumulative = 0
    self.interestCumulative = 0

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

  def capRepayment(self):
    if self.balance + self.interest < self.repayment:
      self.setRepayment(self.balance + self.interest)

  def performTransactions(self):
    self.offsetBalance(self.interest - self.repayment)
    self.repaymentCumulative = round(self.repaymentCumulative + self.repayment, 2)
    self.interestCumulative = round(self.interestCumulative + self.interest, 2)

  def setInterestRate(self, newInterestRate):
    self.interestRate = newInterestRate

  def calculateInterest(self):
    self.interest = Calc.getMonthlyInterest(self.balance, self.interestRate)

  def incrementTermCurrent(self):
    self.termCurrent += 1
    self.termRemaining -= 1






