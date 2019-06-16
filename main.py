# Script to simulate financial outgoings


##################################################
# IMPORTS
##################################################

# Custom modules
import Components
import Calc
import Results

# Common Python modules
import pandas as pd
import math


##################################################
# USER INPUTS
##################################################

# Number of months to simulate
simulationLength = 100*12

# Initialise settings dict
settings = {}

# Income
settings['income'] = {
  'salary': 31500,
  'salariseRiseRate': 0.03
}

# Mortgage settings
settings['mortgage'] = {
  'balance': 130195,
  'interestRateFixed': 0.0212,
  'termLength': 300,
  'interestRateVariable': 0.0424,
  'interestRateVariableIntroduction': 64
}

# Student Finance
settings['slc'] = {
  'balance': 26104.72,
  'repaymentThreshold': 25725,
  'repaymentFraction': 0.09,
  'interestRateSalaryLowerBound': 25725,
  'interestRateSalaryUpperBound': 46305,
  'interestRateAdditionLowerBound': 0,
  'interestRateAdditionUpperBound': 0.03,
  'RPI': 0.033
}

##################################################
# Initialise
##################################################

# Mortgage
mortgage = Components.Loan('Mortgage',
  settings['mortgage']['balance'],
  settings['mortgage']['interestRateFixed'],
  1,
  settings['mortgage']['termLength'])

# Student Loan
settings['slc']['interestRateSalaryRange'] = settings['slc']['interestRateSalaryUpperBound'] - settings['slc']['interestRateSalaryLowerBound']
settings['slc']['interestRateAdditionRange'] = settings['slc']['interestRateAdditionUpperBound'] - settings['slc']['interestRateAdditionLowerBound']
slc = Components.Loan('Student Finance',
  settings['slc']['balance'],
  0.033,
  1,
  30*12
)

##################################################
# Main Solve
##################################################

for nMonth in range(1, simulationLength+1):

  ##################################################
  # Initialise results storage
  result = Results.Result(nMonth)

  ##################################################
  # Mortgage
  if mortgage.termCurrent <= settings['mortgage']['termLength']:

    # Check if moving from fixed to variable rate
    if nMonth is settings['mortgage']['interestRateVariableIntroduction'] :
      mortgage.setInterestRate(settings['mortgage']['interestRateVariable'])

    # Calculate the interest to be added
    mortgage.calculateInterest()

    # Calculate the amount to repay this month
    mortgage.calculateRepayment()
    mortgage.capRepayment()

    # Perform the transactions
    mortgage.performTransactions()

    # Save the results
    result.saveMortgage(mortgage)

    # Update the mortgage term remaining
    mortgage.incrementTermCurrent()
  
  ##################################################
  # Student Finance
  if slc.termRemaining >= 0 and slc.balance > 0:

    # Calculate new interest rate
    salary = 31500
    salaryScale = (salary-settings['slc']['interestRateSalaryLowerBound']) / settings['slc']['interestRateSalaryRange']
    slc.setInterestRate(settings['slc']['RPI'] + settings['slc']['interestRateAdditionLowerBound'] + salaryScale*settings['slc']['interestRateAdditionRange'])

    # Set the repayment amount
    slc.setRepayment(settings['slc']['repaymentFraction'] * (salary-settings['slc']['repaymentThreshold']) / 12)
    slc.capRepayment()

    # Perform the transactions
    slc.performTransactions()

    # Update the mortgage term remaining
    slc.incrementTermCurrent()

    # Save the results
    result.saveSLC(slc)

  ##################################################
  # Collate results


##################################################
# Post Solve
##################################################

print('Simulation Complete.')


