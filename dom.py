import math

def funkciika(num):
    num1 = num
    count = 1
    while num >= 2:
        num = math.sqrt(num)
        count += 1
	
    return count

def findLength(string): 
  
    count = 0

    for i in string: 
        count+= 1

    return count 
  
string = "12345"
print("Lenght", findLength(string))

p = int(input("Enter a number: "))

print(funkciika(p))
