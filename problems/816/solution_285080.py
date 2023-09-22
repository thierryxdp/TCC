def maiores(lista,n):
    '''cria uma lista com os números maiores que "n"presentes numa lista'''
    lista_ordenada=lista.sort()
    
    lista_nova=list.index(lista_ordenada>n)
    
    return lista_nova