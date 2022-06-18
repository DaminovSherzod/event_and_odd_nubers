#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".

var_int = 2468
x1 = var_int % 10
var_int //= 10

x2 = var_int % 10
var_int //= 10

x3 = var_int % 10
var_int //= 10

x4 = var_int % 10
s = x1%2 + x2%2 + x3%2 + x4%2
print(s)