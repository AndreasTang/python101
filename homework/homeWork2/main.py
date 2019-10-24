# disign a order system which have 4 meals and their price, user can order their meals and enter -1 for end input 
# list how many meals are order and how much money we earn
# sort the order from high to low

print('Welcome to Full Belly steak house!!')
print('You can enter 1 to enter meals order system or enter 2 to enter meals counter system')

codeSelection = int(input('What do you want ? (1 for meals order / 2 for meals counter) :'))

if codeSelection == 1:

    mealsOrderSystem()

elif codeSelection == 2:

    mealsCounterSystem()

else:

    errorMessage()



print(mealsOrder)


    # beefSteak = int(input('How many beefSteak you want to order: '))
    # porkSteak = int(input('How many porkSteak you want to order: '))
    # fishSteak = int(input('How many fishSteak you want to order: '))
    # beefAndSeafoodSteak = int(input('How many beefAndSeafoodSteak you want to order: '))

