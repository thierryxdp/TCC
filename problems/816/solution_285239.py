def maiores(lista,n):
    ''' função que dado uma lista e um numero retorna
    os numeros maiores que ele dentro da lista
    list,int---> list'''
    if n in lista:
        partida = list.index(lista,n)
        if list.count(lista,n) >1:
            excesso = list.count(lista,n)
            return lista[partida + 1 - excesso:]
        else:
            return lista[partida+1:]
    else:
        lista.append(n)
        list.sort(lista)
        partida = list.index(lista,n)
        return lista[partida+1:]