import menu

def individualOrder(meal):

    isInteger = False

    while isInteger == False:

        try:

            individualMeals = float(input('How many {:s} you want to order: '.format(meal)))

            if "." in individualMeals:

                print('Invalid input, we only accept integer, please try again')
            
            else:

                individualMeals = int(individualMeals)
                isInteger = True

        
        except:

            print('Invalid input, we only accept integer, please try again')

    return  individualMeals
        


def mealsOrderSystem():

    mealsOrder = map(menu)

    print('Welcome to Full Belly steak house order system')
    print('Please enter your name and phone number first')

    customerName = input('Your name: ')
    customPhoneNumber = input('Your phone number: ')

    print('For order meals, Please enter the number of meal you want to order individual, we only accept integer')
    print('You can also enter -1 to skip the rest of order process anytime if any orders are made, this will lead you to bill section')

    for i in range(len(menu)):

        meals = individualOrder(mealsOrder[meals][i])
        mealsOrder[counter][i] = meals

    return mealsOrder