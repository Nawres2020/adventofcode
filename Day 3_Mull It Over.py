#--- Day 3: Mull It Over ---
import re
def mull(text):
    matche_mul = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)
    multip = 0
    for x ,y in matche_mul:
        multip = multip + int(x)*int(y)
    return multip

# Lets test it on the providd text in the example 
example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
multip_example =mull(example)
print('the results of the multiplications',multip_example)
# i saved the puzzle input in a text file called day3_data we need to read it 
with open("C:/Users/21629/Desktop/code/day3_data.txt", "r") as fichier:
    day3_data = fichier.read()
    multip = mull(day3_data)
print('the results of the multiplications',multip)
#the results of the multiplications = 173529487

#--- Part Two ---
# Lets define a function that will deal with the do and dont instruction and apply our mull function 

def do_dont(text):
    matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", text)
    enabled = True
    liste = []

    for match in matches:
        t = match.group(0)
        if t == "do()":
            enabled = True
        elif t == "don't()":
            enabled = False
        elif t.startswith("mul(") and enabled:
            liste.append(t)
    final_text = ''.join(liste)
    return mull(final_text)
example2="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
print('the results of just the enabled multiplications',do_dont(example2))
# its correct for the example , lets try it on the puzzle input
with open("C:/Users/21629/Desktop/code/day3_data.txt", "r") as fichier:
    day3_data = fichier.read()
    multip2 = do_dont(day3_data)
print('the results of just the enabled multiplications',multip2)
#the results of just the enabled multiplications = 99532691