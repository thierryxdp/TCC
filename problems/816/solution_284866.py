def maiores(lista,n):
    '''Retorna outra lista com todos os numeros maiores que n
    em ordem crescente; list,int->list'''
    if n in lista:
        lista.sort(lista)
        lista2=lista[list.index(lista,n) + 1:]
        return lista2
    else:
        list.append(lista,n)
        list.sort(lista)
        lista2= lista[list.index(lista,n) + 1:]
        return lista2