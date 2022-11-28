# CTI-110
# P4HW1 - Score List
#Noah Kolb
#11/14/22
#
#loop number input
inputs = 1
Slist=[-1]
print("How many scores do you want to enter?  ",end=' ')
scores = int(input())
print()
#while loop, list creation
while inputs <= scores:
    print (f'Enter score #{inputs}:',end=' ')
    score = float(input())
    if score < 0:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
    elif score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
    else:
        Slist.append(score)
        inputs = inputs+1
Slist.remove(-1)
print()
#average calculations& grade
average = sum(Slist)/len(Slist)
if average >= 90:
    grade = ('A')
elif average >= 80:
    grade = ('B')
elif average >= 70:
    grade = ('C')
elif average >= 60:
    grade = ('D')
else:
    grade = ('F') 
#result display
print('-------------------------------------Results------------------------------------')
print('Lowest Score   :',min(Slist))
print('Modifies List  :',Slist)
print('Scores Average :',"%.1f" % average)
print('Grade          :',grade) 
print('--------------------------------------------------------------------------------')
