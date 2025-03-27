# a code that makes a machine gives menu for order 
emo = '(+ n +)'

def decision(speak):
    print(speak,emo)

#get data
def main():
    global emo
    MENU = ['salad','juice', 'Pie']
    name = input('hello there what is your name ?\n').title().strip()

#compute the condition
    print('\nMENU:')
    for  menu in MENU:
        print(menu,'\n')

    food = input('ok ' + name + ' from the menu above what food will you like today ?\n').title().strip()

    if 'salad' in food:
        emo = '(> - 0)'
        decision('ok! '+name+' noted! your '+food+ ' will arrive soon')
    elif 'juice' in food:
        emo = '(> O <)'
        decision('ok! '+name+' noted! your '+food+ ' will arrive soon')
    elif 'Pie' in food:
        emo = '(0 - <)'
        decision('ok! '+name+' noted! your '+food+ ' will arrive soon')
    else:  
        emo = '(X _ X;)'
        decision("hello "+name+" "+food+ " is not on the list. try choosing again")
main()