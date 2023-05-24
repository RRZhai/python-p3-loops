#!/usr/bin/env python3

count = 10
def happy_new_year():
    count = 10
    while count >= 1:
        print(f'{count}')
        count -= 1
    print('Happy New Year!')


def square_integers(int_list):
    square_list = []
    for item in int_list:
        square_int = item*item
        square_list.append(square_int)
    return square_list

def fizzbuzz():
    count = 1
    while count <= 100:
        if count%3 == 0 and count%5==0:
            print("FizzBuzz")
        elif count%5 == 0:
            print('Buzz')
        elif count%3 == 0:
            print('Fizz')
        else: 
            print(f'{count}')
        count +=1