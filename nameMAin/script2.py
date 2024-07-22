from script1 import *


def favorite_drink(drink):
    print(f'Your favorite is {drink}')


def main():
    print("This is script2")
    favorite_food("Sushi")
    favorite_drink("coffee")
    print('Goodbye')


if __name__ == '__main__':
    main()
