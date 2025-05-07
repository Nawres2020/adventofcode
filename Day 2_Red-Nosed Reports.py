#--- Day 2: Red-Nosed Reports ---
import pandas as pd

# for a first test i convert the example to matrice 
L1 = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

#starting by calculating the differences between adjacent elements in a L1 in a function
def safe_unsafe(list):
    difference = [list[i+1] - list[i] for i in range(len(list) - 1)]
    
    if all(1 <= d <= 3 for d in difference):  # this is strictly increasing 
       return True 
    elif all(-3 <= d <= -1 for d in difference):   # decreasing
        return True  
    else:
        return False 
count = 0
for i in L1 :
    if safe_unsafe(i)  :
        count = count + 1
#print("The number of safe reports are =" , count)

##### Lets try it on our puzzle input that i saved as csv : day2.csv
# i tried to open it with pandas but pandas force to have same number on colones for each line
safe_count = 0 
with open("C:/Users/21629/Desktop/code/day2.csv", "r") as file:
    for line in file:
        report = list(map(int, line.strip().split(",")))
        if safe_unsafe(report):
            safe_count =  safe_count +1
print("The number of safe reports are =" , safe_count)

#The number of safe reports are = 279
# we will all another function to remove a single level from an unsafe report and test it

#--- Part Two ---
def safe_tole(list):
    if safe_unsafe(list):
        return True
    for i in range(len(list)):
        new_list = list[:i] + list[i+1:]
        if safe_unsafe(new_list):
            return True
    return False

# i will test it before on the example 
count = 0
for i in L1 :
    if safe_tole(i)  :
        count = count + 1
print("--- Part Two ---")
#print("The number of safe reports are =" , count)

# it workes :D 
# test it on our puzzle data 
safe_count = 0 
with open("C:/Users/21629/Desktop/code/day2.csv", "r") as file:
    for line in file:
        report = list(map(int, line.strip().split(",")))
        if safe_tole(report):
            safe_count =  safe_count +1
print("The number of safe reports are =" , safe_count)

#The number of safe reports are = 343