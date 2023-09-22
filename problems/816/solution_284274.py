def maiores(l, n):
    """"""
    lnova = l + [n]
    lnova.sort()
    i = list.index(lnova, n)
    return lnova[i+1:]
#Teste 1:
#maiores([1, 2, 4, 5, 7, 9], 6)--> [7, 9]

#Teste 2:
#maiores([2, 45, 34, 440], 120)--> [440]