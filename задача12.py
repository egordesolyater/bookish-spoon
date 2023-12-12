#Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.Формат ввода следующий:В первой строке указано целое число n — количество завершенных игр.После этого идет n строк, в которых записаны результаты игры в следующем формате:Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командойВывод программы необходимо оформить следующим образом:Команда:Всего_игр Побед Ничьих Поражений Всего_очковКонкретный пример ввода-вывода приведён ниже.Порядок вывода команд произвольный.

arr=[]
book={}
n=int(input())
for i in range(n):
  sz=input().split(";")
  if sz[0] not in book.keys():
    book[sz[0]]=[0,0,0,0,0] # ВсегоИгр Победы Ничьи проигрышы очки
  if sz[2] not in book.keys():
    book[sz[2]]=[0,0,0,0,0]
  if int(sz[1])==int(sz[3]):
    book[sz[0]][0]+=1
    book[sz[0]][2]+=1
    book[sz[0]][4]+=1
    book[sz[2]][0]+=1
    book[sz[2]][2]+=1
    book[sz[2]][4]+=1
  elif int(sz[1])<int(sz[3]):
    book[sz[2]][0]+=1
    book[sz[2]][1]+=1
    book[sz[2]][4]+=3
    book[sz[0]][0]+=1
    book[sz[0]][3]+=1
    book[sz[0]][4]+=0
  else:
    book[sz[0]][0]+=1
    book[sz[0]][1]+=1
    book[sz[0]][4]+=3
    book[sz[2]][0]+=1
    book[sz[2]][3]+=1
    book[sz[2]][4]+=0



print(book)
  
