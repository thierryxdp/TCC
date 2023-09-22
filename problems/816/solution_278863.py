listaMaiores = []

def maiores(L,n):
    for i in L:
        if i > n:
            listaMaiores.append(i)
            i.sort()
    return listaMaiores