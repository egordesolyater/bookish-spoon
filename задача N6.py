#Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file,'r') as text:
     words = text.read().split()
    max_length = len(max(words, key=len))
    arr_words = [word for word in words if len(word) == max_length]
    if len(arr_words) == 1:
        return arr_words[0]
    return arr_words

print(longest_words('text.txt'))
