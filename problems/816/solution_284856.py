def maiores(lista,n):
    '''Retorna outra lista com todos os numeros maiores que n
    em ordem crescente; list,int->list'''
    lista.append(lista,n)
    lista.sort(lista)
    lista2= lista.sort(lista) + lista
    return lista2