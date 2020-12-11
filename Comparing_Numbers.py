print("WELCOME TO NUMBER COMPARE")
print("Designed and Programmed By Ayaan Ansari")
print("Please Type your First number:")
var1 = int(input())
print("Please type your second number:")
var2 = int(input())
if var1 > var2:
    print(var1 , "is greater than"  , var2)
elif var2 > var1:
    print(var2,"is greater than",var1)
else:
    print("Both numbers are equal")