def repetidos (listanum):
    '''Função que recebe uma lista de números e retorna o números de vezes que o elemento da lista é igual ao elemento anterior.
    list -> int.'''
    indice = 0
    resposta = 0
    while indice is not len (listanum):
        if listanum[indice+1] == listanum[indice]:
            resposta = resposta +1
        indice = indice +1
        if indice == len(listanum)-1:
            return resposta