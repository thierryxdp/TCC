def insere(lista_numero,n):
    '''função que recebe uma lista ordenada crescente de números inteiros
    e um número n, e retorna n em uma posição em que a lista continue 
    ordenada
    list,int->list'''
    
    list(lista_numero)
    lista_numero.append(n)
    lista_ordenada=sorted(lista_numero)
    return lista_ordenada