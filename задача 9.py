# Напишите программу на Python для преобразования десятичного числа в двоичное число.

a=int(input())
s=''
while True:
  s+=str(a%2)
  a//=2
  if a<=1:
    s+="1"
    break
print(s[::-1])

#Для восьмеричной 
a=int(input())
s=""
while True:
  s+=str(a%8)
  a//=8
  if a<8:
    s+=str(a)
    break

print(s[::-1])
#для шестнадцатиричной 
a=int(input())
s=""
while True:
  s+=str(a%16)
  a//=16
  if a<16:
    s+=str(a)
    break  
print(s[::-1])
