# Script to simulate financial outgoings


##################################################
# IMPORTS
##################################################

import Components
import Calc



##################################################
# USER INPUTS
##################################################

# Number of months to simulate
simulationLength = 100*12

# Initialise settings dict
settings = {}

# Mortgage settings
settings['mortgage'] = {}
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
  # Mortgage
  if mortgage.termRemaining > 0:

    # Check if moving from fixed to variable rate
    if nMonth is settings['mortgage']['interestRateVariableIntroduction'] :
      mortgage.setInterestRate(settings['mortgage']['interestRateVariable'])

    # Calculate the interest to be added
    mortgage.calculateInterest()

    # Calculate the amount to repay this month
    mortgage.calculateRepayment()
    if mortgage.balance + mortgage.interest < mortgage.repayment:
      mortgage.repayment = mortgage.balance + mortgage.interest

    # Action the repayment
    mortgage.offsetBalance(mortgage.interest - mortgage.repayment)

    # Update the mortgage term remaining
    mortgage.decrementTermRemaining()
  
  ##################################################


##################################################
# Post Solve
##################################################

print('Simulation Complete.')


