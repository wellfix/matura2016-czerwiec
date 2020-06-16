plik = open("liczby.txt").read().split()

licznik = 0

for x in plik:
    s = int(x[len(x)-1])
    x = x[:len(x)-1]
    if s == 8:
        licznik+=1

print(licznik)