#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".

var_int = 2346
sum_even = 0
x1 = var_int%10
var_int //= 10

x2 = var_int%10
var_int //= 10

x3 = var_int%10
var_int //= 10

x4 = var_int%10
var_int //= 10
s1 = (x1+1)%2
s2 = (x2+1)%2
s3 = (x3+1)%2
s4 = (x4+1)%2
b1 = s1 * x1
b2 = s2 * x2
b3 = s3 * x3
b4 = s4 * x4
sum_even = b1 + b2 + b3 + b4
print(sum_even)