#This is for LIN 5932, Assignment 3: Github and Numerics, Susan Cox
#This code will take a number and check its type, which the output should be class str, then convert the number to class int and add 10, then it will convert it to a binary then a hexadecimal output

#Enter the number here
num = input()

#Print the type (Should output 'str')
print(type(num))

#Change string to integer
x = int(input("Enter the number again to covert str to int and add 10:"))
y = int(x)
print("You have entered", y)

#The str is converted to an integer and increased by 10
converted_num = int(num)
print("Type After Conversion:", type(converted_num))
print(converted_num + 10)

#Convert the decimal/base 10 number to a binary/base 2 number

def DecimalToBinary(n):
    return "{0:b}".format(int(n))
   
#This will convert input + 10 to binary
print(DecimalToBinary((converted_num + 10)))

#Convert the decimal/base 10 number to a hexadecimal/base 16 number

def DecimalToHexadecimal(n):
    return "{0:x}".format(int(n))
   
#This will convert input + 10 to hexadecimal
print(DecimalToHexadecimal((converted_num + 10)))


         











