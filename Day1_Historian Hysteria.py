#--- Day 1: Historian Hysteria ---


import pandas as pd 
#here to test the results of the exercice 
L1=[3 ,4 ,2 ,1 ,3 ,3]
L2 =[4,3,5,3,9,3]

# My idea to put the inut inside an CSV and use it 
#starting by reading the file 
data_day1=pd.read_csv("C:/Users/21629/Desktop/code/day_one.csv",header=None)
#here i sorted the list because  the distance is smallest number in the left list with the smallest number 
# in the right list, then the second-smallest with the second-smallest, and so on
left_sorted = sorted(data_day1[0])
right_sorted = sorted(data_day1[1])

# the distance calculation 

distance =  sum(abs(i - j) for i, j in zip(left_sorted, right_sorted))
print("The total distance between My  lists = " , distance)

# The total distance between My  lists = 2196996
#--- Part Two ---
# i can use count here but i would like to try with 2 boucles imbriqué 
list_similarity= []
for i in data_day1[0]:
    similarity = 0
    for j in data_day1[1]:
        if i == j:
            similarity =similarity +1 
    list_similarity.append(i*similarity)   


calcule_similarity = sum(list_similarity)
print(" The similarity score =",calcule_similarity)
# The total distance between My  lists = 23655822