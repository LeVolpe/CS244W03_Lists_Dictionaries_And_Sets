import sys

stock = {
    "apple": 10,
    "strawberry": 35,
    "orange": 9,
    "beetroot": 20,
    "carrot": 13
}

prices = {
    "apple": 1.4,
    "strawberry": 2.0,
    "orange": 1.0,
    "beetroot": 2.5,
    "carrot": 1.2
}

cymraeg = {
    "apple": "afal",
    "strawberry": "mefus",
    "orange": "oren",
    "beetroot": "betys",
    "carrot": "moron"
}

customer1 = ["apple", "orange", "apple", "beetroot", "beetroot"]

def calculateStockVal():

    product = 0

    for key in stock:
        print(key, 'corresponds to', stock[key], ' * ', prices[key], ' = ', stock[key] * prices[key])
        product = product + (stock[key] * prices[key])

    print('This is the product: ', product, '\n')

def calculateCustomerList(products):

    total = 0
    for key in products:
        total = total + prices[key]
        stock[key] = stock[key] - 1
        print('Removing one of: ', key, ' and new value: ', stock[key])

    print('Customer pays: £', total, '\n')

def getInput():
    for line in sys.stdin:
        return line.strip()

def exists(product):
    exist = 0
    for key in stock:
        if key == product:
            exist = 1

    return exist

def newStock():
    print('Stock name: ')
    stockName = getInput()
    print('\n', str(stockName), 'in Welsh: ')
    welshName = getInput()
    print('\n', str(stockName), ' price: ')
    price = getInput()
    print('\n', str(stockName), ' in Stock: ')
    stockNumber = getInput()

    print('stockName ', stockName)
    print('welshName ', welshName)
    print('price ', price)
    print('stockNumber ', stockNumber)

    print('Before: ')
    print(stock)
    print(prices)
    print(cymraeg)

    print('Updating: ')
    stock[stockName] = stockNumber
    prices[stockName] = price
    cymraeg[stockName] = welshName

    print('After: ')
    print(stock)
    print(prices)
    print(cymraeg)

def printEnglishMenu():
    for key in stock:
        print(key, ' for ', prices[key])

    print('\n')


def printWelshMenu():
    for key in stock:
        print(cymraeg[key], ' for ', prices[key])

    print('\n')

def printMenu():
    print('1: To calculate stock value.')#
    print('2: Insert new stock')
    print('3: English menu')
    print('4: Welsh menu')

def menu():
    input = ''
    while input != 'q':
        input = getInput()

        if input == '1':
            calculateStockVal()
        elif input == '2':
            newStock()
        elif input == '3':
            printEnglishMenu()
        elif input == '4':
            printWelshMenu()

menu()