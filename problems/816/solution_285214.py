def maiores(lista,n):
    if n in lista:
        partida=list.index(lista,n)
        if list.count(lista,n) >1:
            excesso =list.count(lista,n)
            return lista[partida + 1 - excesso:]
        else:
            return lista[partida:]