insere(lista_numero,n):
    '''recebe uma lista de numeros ordenados no 1 arg e retorna 
    uma lista tambem ordenada com o segundo arg adicionado
    list , complex -> list'''
    
    nova_lista = list.append(lista_numero,n)
    
    return list.sort(nova_lista)