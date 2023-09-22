def repetidos(lista):
    '''Funcao que retorna a quantidade de vezes em que um elemento da lista é igual
    ao elemento anterior. 
    List -> Str'''
    indice = 0
    quantidade = 0
    while indice<len(lista)-1:
        if lista[indice] == lista[indice +1]:
            quantidade = quantidade + 1
        indice = indice + 1
    return quantidade