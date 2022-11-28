initialDeposit = 45
interestPerYear = 0.021

for i in range(0,3):
    initialDeposit = initialDeposit + (initialDeposit * interestPerYear)

print(round(initialDeposit, 2))