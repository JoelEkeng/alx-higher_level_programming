#!/bin/usr/python3
for i in range (0,100):
    if i in range(0,10):
        print (f"0{i},", end="")
    if i in range (10,100):
        print (f"{i},", end="")
