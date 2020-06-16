plik = open("liczby.txt").read().split()

licznik = 0

for x in plik:
    s = int(x[-1])
    x = x[:-1]
    if s == 8:
        licznik+=1

print(licznik)