def lista(x):
    i = 0
    cont = x
    lista = []
    while i < x:
        list.append(lista,cont)
        cont -= 1
        i += 1
    return list.sort(lista)


def faltante(n):
    i = 0
    peca = 0
    list.sort(n)
    while len(lista(x)) != len(n):
        if not n[i] == n[i-1] + 1:
            peca = n[i] - 1
            list.append(n,n[i] - 1)
        else:
            peca = n[-1] +1
            list.append(n,n[-1] +1)
        i += 1    
    return peca