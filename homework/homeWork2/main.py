# disign a order system which have 4 meals and their price, user can order their meals and enter -1 for end input 
# list how many meals are order and how much money we earn
# sort the order from high to low

from functions import mealsOrderSystem
from functions import mealsCounterSystem
from functions import errorMessage
from functions import writeOrders

isPass = False

print('Welcome to Full Belly steak house!!')
print('You can enter 1 to enter meals order system or enter 2 to enter meals counter system, -1 to exit system')

while isPass == False:

    codeSelection = int(input('What do you want ? (1 for meals order / 2 for meals counter / -1 to exit) : '))

    if codeSelection == 1:

        isPass = True
        mealsOrder =  mealsOrderSystem()
        print(mealsOrder)
        writeOrders(mealsOrder[0]['name'], mealsOrder)

    elif codeSelection == 2:

        isPass = True
        mealsCounterSystem()

    elif codeSelection == -1:

        isPass = True
        print('Exited')

    else:

        errorMessage()




