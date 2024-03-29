# Code to collate simulation results

import pandas as pd
import math

class Result:
  def __init__(self, index):
    self.index = index

    self.initialiseValues()

  def initialiseValues(self):
    nan = math.nan

    # Mortgage
    self.mortgage__balance              = nan
    self.mortgage__interestRate         = nan
    self.mortgage__interest             = nan
    self.mortgage__termCurrent          = nan
    self.mortgage__repayment            = nan

    # Student Finance
    self.slc__balance                   = nan
    self.slc__interestRate              = nan
    self.slc__interest                  = nan
    self.slc__termCurrent               = nan
    self.slc__repayment                 = nan

  def saveMortgage(self, mortgage):
    self.mortgage__balance              = mortgage.balance
    self.mortgage__interestRate         = mortgage.interestRate
    self.mortgage__interest             = mortgage.interest
    self.mortgage__termCurrent          = mortgage.termCurrent
    self.mortgage__repayment            = mortgage.repayment

  def saveSLC(self, slc):
    self.slc__balance                   = slc.balance
    self.slc__interestRate              = slc.interestRate
    self.slc__interest                  = slc.interest
    self.slc__termCurrent               = slc.termCurrent
    self.slc__repayment                 = slc.repayment