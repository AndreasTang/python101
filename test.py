
isPass = False

while isPass == False:

    try:

        testMessage = (input('input anything: '))
        testMessage = int(testMessage)
        isPass = True
        print(testMessage)
        print(isPass)

    except:

        print('oh shit')



    
    


