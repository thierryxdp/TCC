def repetidos(lista_num):
    '''Função que dada uma lista de números, retorna quantas vezes um elemento da
    lista é igual ao elemento anterior.
    lista_num -> list
    return -> int'''
    
    i = 1
    lista = lista_num
    contador = 0
    
    while i < len(lista_num):
        if lista[i] == lista[i-1]:
            contador+= 1
        i += 1
    return contador