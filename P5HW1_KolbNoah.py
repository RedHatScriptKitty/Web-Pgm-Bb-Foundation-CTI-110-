# Math quiz
# 11/28/22
# CTI-110 P5HW2 - Math Quiz
# Noah kolb
#
import random
loop = True
while loop == True :
    print("MAIN MENU")
    print("------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print("Please choose one of the menu options: ",end=' ')
    guess=0
    inp =  input()
    if (inp != '1')and (inp != '2')and (inp != '3'):
        print()
        print(inp, "is NOT an option")
        print()
        
    if inp == '1':
        number1 = random.randint(1,100)
        number2 = random.randint(1,100)
        corAns = number1+number2
        print(' ',number1)
        print('+',number2)
        print()
        print('Enter answer')
        ans = int(input())
        while ans != corAns:
            if ans > corAns:
                 print('Sorry, guess is too high')
                 print()
                 print('Try again',end=' ')
                 ans = int(input())
                 guess = guess+1
            elif ans < corAns:
                 print('Sorry, guess is too low')
                 print()
                 print('Try again',end=' ')
                 ans = int(input())
                 guess = guess+1
        if ans == corAns:
            guess = guess+1
        print("Congradulations!!!! your answer is correct..")
        print("number of guesses:", guess)
        print()

    if inp == '2':
        number1 = random.randint(1,100)
        number2 = random.randint(1,100)
        corAns = number1-number2
        print(' ',number1)
        print('-',number2)
        print()
        print('Enter answer')
        ans = int(input())
        while ans != corAns:
            if ans > corAns:
                 print('Sorry, guess is too high')
                 print()
                 print('Try again',end=' ')
                 ans = int(input())
                 guess = guess+1
                 
            elif ans < corAns:
                 print('Sorry, guess is too low')
                 print()
                 print('Try again',end=' ')
                 ans = int(input())
                 guess = guess+1
        if ans == corAns:
            guess = guess+1
        print("Congradulations!!!! your answer is correct..")
        print("number of guesses:", guess)
        print()


        
    elif inp == '3':
        loop = False
        print()
        print("Thank you for playing. . .")
        print("Bye!!")
    
