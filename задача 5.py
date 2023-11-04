#Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле article.txt со следующим содержимым:


def read_last(lines,file):
  with open(file,'r') as inf:
    arr=[]
    for line in inf:
         arr.append(line[:-2])
    arr.reverse()
    for i in range(lines):
      print(arr[i])
      
read_last(3,'text.txt')   
