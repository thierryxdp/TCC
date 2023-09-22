def maiores(lista,n):
    if (n in lista)==True:
        return lista[:(list.index(lista,n)-1)]
    else:
        list.sort(lista)
        if n<lista[0]:
            return lista
        elif n>lista[-1]:
            return []
        elif n>lista[0] and n<lista[1]:
            list.pop(lista,0)
            return lista
        elif n<lista[-1] and n>lista[(len(lista)-2)]:
            return [lista[-1]]
        else:
            return [lista[(len(lista)-2):len(lista)]