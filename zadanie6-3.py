plik = open("liczby.txt").read().split()

licznik = 0

for x in plik:
    s = int(x[len(x)-1])
    x = x[:len(x)-1]
    if s == 2:
        if x[len(x)-1] == '0':
            licznik+=1

print(licznik)