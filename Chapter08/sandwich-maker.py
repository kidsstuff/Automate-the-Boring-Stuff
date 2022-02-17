import pyinputplus as pyip
def getPrice(item):
    cost = {'wheat': 1, 'white': 2, 'sourdough': 3, 'chicken': 4, 'turkey': 5, 'ham': 6, 'tofu': 7, 'cheddar': 1, 'Swiss': 2, 'mozzarella': 3, 'mayo': 0.5, 'mustard': 0.5, 'lettuce': 0.5, 'tommato': 0.5}
    return cost[item]


totalCost = 0
choice = pyip.inputMenu(['wheat', 'white', 'sourdough']) 
totalCost += getPrice(choice)
choice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
totalCost += getPrice(choice)
response = pyip.inputYesNo('Do you want cheese?') 
if response == 'yes':
    choice =  pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella']) 
    totalCost += getPrice(choice)
for item in ['mayo', 'mustard', 'lettuce', 'tomato']:
    response = pyip.inputYesNo(f'Do you want {item}?') 
    if response == 'yes':
        totalCost += getPrice(item)
    
number = pyip.inputInt('How many sandwiches do you want?') # how many sandwiches they want
totalCost *= number
print(f'Total cost: {totalCost}$')
