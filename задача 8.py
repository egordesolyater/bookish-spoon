# Напишите программу на Python для расчета расстояния между двумя точками, используя широту и долготу.pow()
import math 

xa=float(input())
xb=float(input())
ya=float(input())
yb=float(input())
ab=math.sqrt(pow((xa-xb),2)+(pow((ya-yb),2)))

print(ab)
