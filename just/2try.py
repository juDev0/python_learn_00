# a code that makes a machine gives menu for order 
emo = '(+ n +)'
def decision(speak):
    return (speak,emo)

#get data
def main():
    global emo,dec
    MENU = ['salad','juice', 'Pie']
    name = input('hello there what is your name ?\n').title().strip()

#compute the condition
    print('\nMENU:')
    for  menu in MENU:
        print(menu,'\n')

    food = input('ok ' + name + ' from the menu above what food will you like today ?\n').lower().strip()
    # juice -> .title() -> Juice
    # pie -> .title() -> Pie
    # HELoo -> .lower() -> heloo


    if 'k' in food:
        emo = '(@ _ -)'
        dec = decision('hello '+name+' you havent choosen from the list yet')
        print(' '.join(dec))
    elif 'salad' in food:
        emo = '(> - 0)'
        dec = decision('ok! '+name+' noted! your '+food+ ' will arrive soon')
        print(' '.join(dec))
    elif 'juice' in food:
        emo = '(> O <)'
        dec = decision('ok! '+name+' noted! your '+food+ ' will arrive soon')
        print(' '.join(dec))
    elif 'pie' in food:
        emo = '(0 - <)'
        dec =decision('ok! '+name+' noted! your '+food+ ' will arrive soon')
        print(' '.join(dec))
    else:  
        emo = '(X _ X;)'
        dec =decision("hello "+name+" "+food+ " is not on the list. try choosing again")
        print(' '.join(dec))
main() 