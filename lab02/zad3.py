from zad2 import lorem
litera_1="jan"[2]
litera_2="brunow"[3]
decreaseTextLetters=lorem.lower()
if litera_1==litera_2:
    count=decreaseTextLetters.count(litera_1)
else:
    count=decreaseTextLetters.count(litera_1)+decreaseTextLetters.count(litera_2)
print(count)