# Your solution to Exercise 8
n= int(input())

output = ""


for i in range (n +1 ,2 ):
  output+= str(i)
  if i == n or n -1 == i :
    break 
  output += " "

print(output)
