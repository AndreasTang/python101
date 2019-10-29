
from menu import menu
import json
import copy
import os
import glob



def mealsOrderSystem():

    mealsOrder = copy.deepcopy(menu)

    print('Welcome to Full Belly steak house order system')
    print('Please enter your name and phone number first')

    customerName = raw_input('Your name: ')
    customPhoneNumber = raw_input('Your phone number: ')

    print('For order meals, Please enter the number of meal you want to order individual, we only accept integer')

    for i in range(len(mealsOrder)):

        meals = orderNumbers(mealsOrder[i]['meals'])
        mealsOrder[i]['counter'] = meals

    mealsOrder.insert(0, {
            'name': customerName,
            'phoneNumber': customPhoneNumber
        })

    return mealsOrder



def orderNumbers(meal):

    isInteger = False

    while isInteger == False:

        try:

            orderNumber = str(input('How many {:s} you want to order: '.format(meal)))

            if "." in orderNumber:

                print('Invalid input, we only accept integer, please try again')
            
            elif '-' in orderNumber:

                print('Invalid input, we only accept postive integer, please try again')

            else:

                orderNumber = int(orderNumber)
                isInteger = True

        
        except:

            print('Invalid input, we only accept integer, please try again')

    return  orderNumber
        


def errorMessage():

    print('The number you type is neither 1 nor 0, did you mean to exit(type -1) ?')



def mealsCounterSystem():
    
    print('welcome to meals counter system')
    print('For count all bills please type 1')
    print('For list all bills please type 2')
    print('For delete bills please type 3')

    isPass = False

    while isPass == False:

        codeSelection = int(input('What do you want ? : '))

        if codeSelection == 1:

            isPass = True
            totalBills = countAllBill()
            printResult(totalBills)
            ending = raw_input('Enter anything to end: ')


        elif codeSelection == 2:

            isPass = True
            listAllBill()
            ending = raw_input('Enter anything to end: ')

        elif codeSelection == 3:

            isPass = True
            fileName = raw_input('Enter the file name which you want to delete: ')
            deleteBill(fileName)
            ending = raw_input('Enter anything to end: ')

        elif codeSelection == -1:

            isPass = True
            print('Exited')

        else:

            errorMessage()



def countAllBill():

    dir = os.path.dirname(__file__)
    workPath = os.path.join(dir, './orders')
    totalOrders = copy.deepcopy(menu)

    try:

        for filePath in glob.glob(os.path.join(workPath, '*.json')):

            with open(filePath, 'r') as f:

                mealsOrder = json.load(f)

            for i in range(len(totalOrders)):

                totalOrders[i]['counter'] += mealsOrder[i+1]['counter']

    except OSError as e:

        print(e)

    else:

        return totalOrders



def listAllBill():

    dir = os.path.dirname(__file__)
    workPath = os.path.join(dir, './orders')
    indexNumber = 0

    try:

        for filePath in glob.glob(os.path.join(workPath, '*.json')):

            indexNumber += 1 

            with open(filePath, 'r') as f:
            
                mealsOrder = json.load(f)

                print('{:d}.{:s}: {:s}=>{:d}, {:s}=>{:d}, {:s}=>{:d}, {:s}=>{:d}'
                .format(indexNumber,
                mealsOrder[0]['name'],
                mealsOrder[1]['meals'],
                mealsOrder[1]['counter'],
                mealsOrder[2]['meals'],
                mealsOrder[2]['counter'],
                mealsOrder[3]['meals'],
                mealsOrder[3]['counter'],
                mealsOrder[4]['meals'],
                mealsOrder[4]['counter'],))

    except OSError as e:
        
        print(e)
    
    else:

        print('List complete')



def deleteBill(fileName):

    dir = os.path.dirname(__file__)
    filePath = os.path.join(dir, './orders/{:s}.json'.format(fileName))

    try:

        os.remove(filePath)

    except OSError as e:

        print(e)

    else:

        print('File name {:s} have been deleted'.format(fileName))



def writeOrders(name, orderData):

    dir = os.path.dirname(__file__)
    filePath = os.path.join(dir, './orders/{:s}'.format(name))

    with open('{:s}.json'.format(filePath), 'w+') as f:
        json.dump(orderData, f)


def printResult(totalBills):

    totalEarned = 0
    sortedBills = sorted(totalBills, key = lambda i: i['counter'], reverse=True)

    print('The meals sell from high to low is: ')

    for i in range(len(sortedBills)):

        earned = sortedBills[i]['price'] * sortedBills[i]['counter']
        totalEarned += earned 
        print('{:s}: {:d} => Earned: {:d}'.format(sortedBills[i]['meals'], sortedBills[i]['counter'], earned))

    print('And the money we totally earn are: ')
    print(totalEarned)