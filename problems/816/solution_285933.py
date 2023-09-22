def maiores(lista_int,n):
    '''lista,int->list
    lista e inteiro de entrada retornando uma lista com somente os valores maiores que n em ordem crescente'''
    list.append(lista_int,n)
    list.sort(lista_int)
    pos=list.index(lista_int,n)
    del lista_int[0:pos+1]
    return lista_int