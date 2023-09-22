def repetidos (listanum):
    '''Função que recebe uma lista de números e retorna o números de vezes que o elemento da lista é igual ao elemento anterior.
    list -> int.'''
    indice = 0
    resposta = 0
    while listanum [indice] != len (listanum):
        if listanum[indice+1] == listanum[indice]:
            resposta = resposta +1
    	return resposta