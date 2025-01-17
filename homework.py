num = int(input("Enter a three digit number "))
digit = len(str(num)) 
temp = 0

for x in str(num) :
  temp = temp + int(x) ** digit

if temp == num :
  print(num, "Is an armstrong number")
else :
    print(num, "Is not an armstrong number")