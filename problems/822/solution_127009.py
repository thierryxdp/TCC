repetidos(listaN):
    '''retorna o numero de vezes que um elemento int da listaN e igual 
    ao termo anterior
    list->int'''
    contador = 0
    vezes = 0
    while contador < len(listaN):
        if listaN[contador]==listaN[contador+1]:
            vezes = vezes + 1
        contador = contador + 1
    return vezes