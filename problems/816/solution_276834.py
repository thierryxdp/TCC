def maiores(lista,n):
    list.sort(lista)
    for c in lista:
        if n>c:
            return notas[list.index(notas,c):]