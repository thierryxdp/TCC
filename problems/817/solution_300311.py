def maiores(lista,n):
    if n in lista:
        partida = list.index(lista,n)
        if list.count(lista,n) >1:
            excesso = list.count(lista,n)
            return lista[partida + 1 - excesso:]
        else:
            return lista[partida:]
    else:
        lista.append(n)
        list.sort(lista)
        partida = list.index(lista,n)
        return lista[partida+1:]
    
def acima_da_media(lista):
    divisor = len(lista)
    dividendo = sum(lista)
    media= dividendo/divisor
    return maiores(lista)