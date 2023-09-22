def maiores(lista_numero,n):
    '''função que retorna de uma lista uma outra lista 
    contendo os valores maiores que n
    list,int-> list'''
    lista=lista_numero
    list.append(lista,n)
    lista_com_n=lista
    list.sort(lista_com_n)
    total_elementos=len(lista_com_n)
    posicao_n=list.index(lista_com_n,n)
    if posicao_n==(total_elementos-1):
        list.clear(lista_com_n)
        return lista_com_n
    elif 0<posicao_n<(total_elementos-1):
        return lista_com_n[posicao_n+1:]