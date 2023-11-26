#На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n х m, заполнив ее числами от 1 до n x m. 

n=int(input())
m=int(input())
arr=[]
co=1
for i in range(n):
  arr2=[]
  for l in range(m):
    arr2.append(co)
    co+=1
  arr.append(arr2)

for j in range(n):
  print(*arr[j])
    
