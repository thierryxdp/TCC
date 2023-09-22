listaMaiores = []

def maiores(L,n):
    for i in L:
        if i > n:
            listaMaiores.append(i)
            return listaMaiores
        else: