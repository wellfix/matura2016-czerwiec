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


max = [248, 111110002]
min = [248 ,111110002]

for x in plik:
    kod = x
    s = int(x[-1])
    x = x[:-1]
    decX = zamiana(x, s)
    if decX > max[0]:
        max = [decX, kod]
    if decX < min[0]:
        min = [decX, kod]

print("Min to: " + str(min)[1:-1])
print("Max to: " + str(max)[1:-1])