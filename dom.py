import math
num = int(input("Enter a number: "))
num1 = num
count = 0
while num >= 2:
	num = math.sqrt(num)
	count += 1
	
print(num1,'->',count)

def findLength(string): 
  
    count = 0

    for i in string: 
        count+= 1

    return count 
  
string = "12345"
print("Lenght", findLength(string))
    
