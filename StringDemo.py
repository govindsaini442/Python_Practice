print("String Testing")
a = "Hello World"
print(len(a)) ## Length of string
print(a[0]) ## Will print first char that is on index 0 in string

print(a.lower()) ## String in lower case
print(a.upper()) ## print string in Upper case

print(a.replace("World","John")) ## replace "World" with "John" keyword
print(a.split()) ## split the string
print(a.split()[0]) ## Print first string
print(a.split()[1]) ## print Second string


####Command line string argument
#x = input("Enter a string:")
#print("You Entered: ",x)

## String addition
str1 = "Hello"
str2 = "Python"
print(str1 +" "+ str2)

## Iterate through a string and find out specific duplicate character
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

##How to find duplicate character in a string
test = "fhgjfhgjfhgjfhgjf"
list = []
listTmp = []
for char in test:     ## interating thorugh the string
    list.append(char) ## Adding element in a List
print(list)

for element in list:  ## Iterating element of the newly created list
    #print(element)
    if element in listTmp:
        pass
    else:
        print("Total Count for",element+":",list.count(element))
    listTmp.append(element)














