def faltante(lista):
    '''funcao que retorna o numero da peça
    que esta faltando no quebra cabeca
    entrada: lista
    saida: inteiro
    '''
    indice=0
    peca= 1
    while indice<len(lista):
        if peca!=lista[indice]:
            return peca
        indice= indice+1
        peca= peca+1
        
    return peca