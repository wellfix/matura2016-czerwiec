plik = open("liczby.txt").read().split()

def zamiana(a , s):
    wyk = len(a)-1
    tab = []
    liczba = 0
    for x in a:
        tab.append(int(x))
    for x in range(len(tab)):
        idx = x
        ok =  s**(wyk-idx)
        liczba+= tab[x]*ok
    return liczba

suma = 0

for x in plik:
    s = int(x[len(x)-1])
    x = x[:-1]
    if s == 8:
        suma+= zamiana(x, s)

print(suma)
