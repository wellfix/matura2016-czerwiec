plik = open("liczby.txt").read().split()

licznik = 0

for x in plik:
    s = int(x[-1])
    x = x[:-1]
    if s == 4:
        if '0' not in x:
            licznik+=1

print(licznik)