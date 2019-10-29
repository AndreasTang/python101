# set five people's height and weight to auto calculate BMI and comment it  for every people
# bmi = weight / height ^ 2
people = [
    {
        'name': 'Buzzy',
        'height': 175,
        'weight': 101
    }, {
        'name': 'Nerine',
        'height': 148,
        'weight': 35
    }, {
        'name': 'Fuzzy',
        'height': 173,
        'weight': 89
    }, {
        'name': 'Komugi',
        'height': 151,
        'weight': 37
    }, {
        'name': 'Andreas',
        'height': 177,
        'weight': 69
    }
]

def getBMI(height, weight):
    BMI = weight / (height/100) ** 2
    return BMI

def getStateMessage(BMI):
    if BMI < 18.5:
        return 'too light'
    elif BMI >= 18.5 and BMI < 24:
        return 'good'
    elif BMI >= 24 and BMI < 27:
        return 'a little bit overweight'
    elif BMI >= 27 and BMI < 30:
        return 'slightly overweight'
    elif BMI >= 30 and BMI < 35:
        return 'overweight'
    elif BMI >= 35:
        return 'obese'

def printMessage(name, BMI, stateMessage):
    print('{:s} has a BMI of {:f}, which is {:s}'.format(name, BMI, stateMessage))

for i in range(len(people)):
    BMI = getBMI(people[i]['height'], people[i]['weight'])
    stateMessage = getStateMessage(BMI)
    printMessage(people[i]['name'], BMI, stateMessage)
