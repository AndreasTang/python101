# comment

def printName(w, h):
    bmi = w / h ** 2
    print('Your bmi is:', bmi)

print('Welcome to bmi calculater')

for i in range(3):

    print('student:', i+1)
    w = int(input(('please input your weight:')))
    h = int(input(('please input your weight:')))
    h = h / 100
    printName(w, h)


    
