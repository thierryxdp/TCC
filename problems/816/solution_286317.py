def maiores(lista,n):
    '''retorna somente os numeros da lista de entrada maiores que n em ordem crescente
       list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    lista=lista[list.index(lista,n):]
    list.remove(lista,n)
    return lista