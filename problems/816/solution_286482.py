def maiores(lista,n):
    '''retorna outra lista ordenada com o número adcionado;
    list, int -> list'''
    list.sort(lista)
    lista_final= []
    for x in lista:
        if x > n:
            lista_final.append(x)
    return lista_final