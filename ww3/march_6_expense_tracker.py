# EXPENSE TRACKER on coffe and donut buisiness
import time
# MONDAY
print('welcome user, lets calaulate your total revenue for the week\n')
print('MONDAY:\r\t')
coffeePrice = int(input('Enter price of coffee\n\r\t'))
coffeeUnitSold = int(input('enter the unit sold\n\r\t'))

donutPrice = int(input('enter price of donut\n\r\t'))
donutUnitSold =int(input('enter the unit sold\n\r\t'))

revenue1 = coffeePrice * coffeeUnitSold
revenue2 = donutPrice * donutUnitSold
dayTotalRevenue = revenue1 + revenue2

netIncome = int(input('Enter the net income for the day\n\r'))
dayExp1 = dayTotalRevenue - netIncome
print(f'\n\tyou had a daily revenue of {dayTotalRevenue} and net income of {netIncome} making your total MONDAY EXPENSE = {dayExp1:,} NGN\n')




#TUESDAY
print('TUESDAY:\r\t')

coffeePrice = int(input('Enter price of coffee\n\r\t'))
coffeeUnitSold = int(input('enter the unit sold\n\r\t'))

donutPrice = int(input('enter price of donut\n\r\t'))
donutUnitSold =int(input('enter the unit sold\n\r\t'))

revenue1 = coffeePrice * coffeeUnitSold
revenue2 = donutPrice * donutUnitSold
dayTotalRevenue = revenue1 + revenue2

netIncome = int(input('Enter the net income for the day\n\r'))
dayExp2 = dayTotalRevenue - netIncome
print(f'\n\tyou had a daily revenue of {dayTotalRevenue} and net income of {netIncome} making your total TUESDAY EXPENSE = {dayExp2:,} NGN\n')




#WEDNESDAY
print('WEDNESDAY:\r\t')

coffeePrice = int(input('Enter price of coffee\n\r\t'))
coffeeUnitSold = int(input('enter the unit sold\n\r\t'))

donutPrice = int(input('enter price of donut\n\r\t'))
donutUnitSold =int(input('enter the unit sold\n\r\t'))

revenue1 = coffeePrice * coffeeUnitSold
revenue2 = donutPrice * donutUnitSold
dayTotalRevenue = revenue1 + revenue2

netIncome = int(input('Enter the net income for the day\n\r'))
dayExp3 = dayTotalRevenue - netIncome
print(f'\n\tyou had a daily revenue of {dayTotalRevenue} and net income of {netIncome} making your total WEDNESDAY EXPENSE = {dayExp3:,} NGN\n')




#THURSDAY
print('THURSDAY:\r\t')

coffeePrice = int(input('Enter price of coffee\n\r\t'))
coffeeUnitSold = int(input('enter the unit sold\n\r\t'))

donutPrice = int(input('enter price of donut\n\r\t'))
donutUnitSold =int(input('enter the unit sold\n\r\t'))

revenue1 = coffeePrice * coffeeUnitSold
revenue2 = donutPrice * donutUnitSold
dayTotalRevenue = revenue1 + revenue2

netIncome = int(input('Enter the net income for the day\n\r'))
dayExp4 = dayTotalRevenue - netIncome
print(f'\n\tyou had a daily revenue of {dayTotalRevenue} and net income of {netIncome} making your total THURSDAY EXPENSE = {dayExp4:,} NGN\n')




#FRIDAY
print('FRIDAY:\r\t')

coffeePrice = int(input('Enter price of coffee\n\r\t'))
coffeeUnitSold = int(input('enter the unit sold\n\r\t'))

donutPrice = int(input('enter price of donut\n\r\t'))
donutUnitSold =int(input('enter the unit sold\n\r\t'))

revenue1 = coffeePrice * coffeeUnitSold
revenue2 = donutPrice * donutUnitSold
dayTotalRevenue = revenue1 + revenue2


netIncome = int(input('Enter the net income for the day\n\r'))
dayExp5 = dayTotalRevenue - netIncome
print(f'\n\tyou had a daily revenue of {dayTotalRevenue} and net income of {netIncome} making your total FRIDAY EXPENSE = {dayExp5:,} NGN\n')



#CALCULATION IF YOU WORKED ON SATURDAY OR SUNDAY
countBusSat, countBusSun= input('''Did you worked on saturday or sunday? 
.type (yes yes) if you worked on both days 
.type (no no) if you didnt work on any day 
.type (yes no) if you worked on saturday but not not on sunday
.type (no yes) if you worked on sunday but not on saturday
\n\r''').strip().split()
if 'yes' in countBusSat and countBusSun:

#SATURDAY
    print('SATURDY:\r\t')

    coffeePrice = int(input('Enter price of coffee\n\r\t'))
    coffeeUnitSold = int(input('enter the unit sold\n\r\t'))

    donutPrice = int(input('enter price of donut\n\r\t'))
    donutUnitSold =int(input('enter the unit sold\n\r\t'))

    revenue1 = coffeePrice * coffeeUnitSold
    revenue2 = donutPrice * donutUnitSold
    dayTotalRevenue = revenue1 + revenue2


    netIncome = int(input('Enter the net income for the day\n\r'))
    dayExp6 = dayTotalRevenue - netIncome
    print(f'\n\tyou had a daily revenue of {dayTotalRevenue} and net income of {netIncome} making your total SATURDAY EXPENSE = {dayExp6:,} NGN\n')
    
 #SUNDAY
    print('SUNDAY:\r\t')

    coffeePrice = int(input('Enter price of coffee\n\r\t'))
    coffeeUnitSold = int(input('enter the unit sold\n\r\t'))

    donutPrice = int(input('enter price of donut\n\r\t'))
    donutUnitSold =int(input('enter the unit sold\n\r\t'))

    revenue1 = coffeePrice * coffeeUnitSold
    revenue2 = donutPrice * donutUnitSold
    dayTotalRevenue = revenue1 + revenue2


    netIncome = int(input('Enter the net income for the day\n\r'))
    dayExp7 = dayTotalRevenue - netIncome
    print(f'\n\tyou had a daily revenue of {dayTotalRevenue} and net income of {netIncome} making your total SUNDAY EXPENSE = {dayExp7:,} NGN\n')
    
    print('calculating expences...\n')
    time.sleep(10)
    totalExp = dayExp1 + dayExp2 + dayExp3 + dayExp4 + dayExp5 +dayExp6 +dayExp7
    print(f'Your daily expences in total (for the week), is {totalExp:,} NGN')

elif 'no' in countBusSat and countBusSun:
    print('calculating expences...\n')
    time.sleep(10)
    totalExp = dayExp1 + dayExp2 + dayExp3 + dayExp4 + dayExp5
    print(f'Your daily expences in total (for the week), is {totalExp:,} NGN')

else:
    #BETWEEN SATURDAY AND SUNDAY
    day = input('What day did you work between saturday and sunday?').upper()
    print(f'{day}:\r\t')

    coffeePrice = int(input('Enter price of coffee\n\r\t'))
    coffeeUnitSold = int(input('enter the unit sold\n\r\t'))

    donutPrice = int(input('enter price of donut\n\r\t'))
    donutUnitSold =int(input('enter the unit sold\n\r\t'))

    revenue1 = coffeePrice * coffeeUnitSold
    revenue2 = donutPrice * donutUnitSold
    dayTotalRevenue = revenue1 + revenue2


    netIncome = int(input('Enter the net income for the day\n\r'))
    dayExp8 = dayTotalRevenue - netIncome
    print(f'\n\tyou had a daily revenue of {dayTotalRevenue} and net income of {netIncome} making your total {day} EXPENSE = {dayExp8:,} NGN\n')
    
    print('calculating expences...\n')
    time.sleep(10)
    totalExp = dayExp1 + dayExp2 + dayExp3 + dayExp4 + dayExp5 +dayExp8
    print(f'Your daily expences in total (for the week), is {totalExp:,} NGN')