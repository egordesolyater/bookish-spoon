# Напишите программу на Python для расчета значений квадратного урав.
from math import sqrt
a=int(input())
b=int(input())
c=int(input())
d=b**2 - 4*a*c
if d<0:
  print("не имеет корней")
elif d==0:
  print((-b)/2*a)
else:
  print(((-b)+sqrt(d))/(2*a))
  print(((-b)-sqrt(d))/(2*a))
