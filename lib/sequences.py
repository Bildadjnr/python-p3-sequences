#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length == 0:
        print (fib_list)
    elif length == 1:
        fib_list = [0]
        print(fib_list)
    else:
        fib_list = [0, 1]  
        for i in range(2, length):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        print(fib_list)
    

print(print_fibonacci)