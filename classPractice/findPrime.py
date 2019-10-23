startNumber = int(input('Please enter start number: '))
endNumber = int(input('Please enter end number: '))

prime = []

def printPrime(startNumber, endNumber):
    for divisor in range(startNumber, endNumber):
        isPrime(startNumber, endNumber)

def isPrime(startNumber, endNumber):
    for dividend in range(2, endNumber):
        if startNumber % dividend != 0:
            print('{:f} / {:f} is a prime'.format(, dividend))
            prime.append(dividend)

print(printPrime(startNumber, endNumber))