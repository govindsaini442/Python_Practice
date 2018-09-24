print("String Testing")
a = "Hello World"
print(len(a)) ## Length of string
print(a[0]) ## Will print first char that is on index 0 in string

print(a.lower()) ## String in lower case
print(a.upper()) ## print string in Upper case

print(a.replace("World","John")) ## replace World with "John" keyword
print(a.split()) ## split the string
print(a.split()[0]) ## Print first string
print(a.split()[1]) ## print Second string


####Command line string argument
x = input("Enter a string:")
print("You Entered: ",x)

## String addition
str1 = "Hello"
str2 = "Python"
print(str1 +" "+ str2)