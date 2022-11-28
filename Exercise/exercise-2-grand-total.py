print('Enter Meal Price')
priceOfMeal = float(input())
taxRate = 0.02 #2% TAX

tax = priceOfMeal * taxRate
tip = (priceOfMeal - tax) * 0.1

print('Meal Price: P' + str(priceOfMeal))
print('Meal Tax(2%): P' + str(tax))
print('Tip: P' + str(tip))