def maiores(lista,n):
    lista1 = sorted(lista)
    if n in lista1:
        posicao = lista.index(n)
        return posicao