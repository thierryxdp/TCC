def repetidos (lista_numeros):
    '''
    função que dada uma lista de números, retorna o número de vezes que um elemento da lista
    é igual ao elemento anterior
    list--> int
    '''

    i=1
    resposta=0
    while i<len(lista_numeros):
        if lista_numeros[i-1]==lista_numeros[i]:
            resposta= resposta+1
        i=i+1

    return resposta