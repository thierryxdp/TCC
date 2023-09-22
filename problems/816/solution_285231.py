def maiores(lista,n):
    partida=list.index(lista,n)
    if n in lista:
        if list.count(lista,n) >1:
            excesso =list.count(lista,n)
            return lista[partida + 1 - excesso:]
        else:
            return lista[partida:]
    else:
        lista.append(n)
        list.sort(lista)
        return lista[partida:]