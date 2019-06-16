# Script to simulate financial outgoings


##################################################
# IMPORTS
##################################################

import Components
import Calc
import Results

import pandas as pd


##################################################
# USER INPUTS
##################################################

# Number of months to simulate
simulationLength = 100*12

# Initialise settings dict
settings = {}

# Mortgage settings
settings['mortgage'] = {
  'balance': 130195,
  'interestRateFixed': 0.0212,
  'termLength': 300,
  'interestRateVariable': 0.0424,
  'interestRateVariableIntroduction': 64
}


##################################################
# Initialise
##################################################

mortgage = Components.Loan('Mortgage', settings['mortgage']['balance'], settings['mortgage']['interestRateFixed'], settings['mortgage']['termLength'])


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
    if mortgage.balance + mortgage.interest < mortgage.repayment:
      mortgage.setRepayment(mortgage.balance + mortgage.interest)

    # Perform the transactions
    mortgage.performTransactions()

    # Update the mortgage term remaining
    mortgage.incrementTermCurrent()

    # Save the results
    result.saveMortgage(mortgage)
  
  ##################################################


##################################################
# Post Solve
##################################################

print('Simulation Complete.')


