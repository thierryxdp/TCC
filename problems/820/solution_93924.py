def posLetra (frase, letra, ocorrencia):
    '''Função retorna em qual índice de posição da ocorrência da letra está na string. 
    str, str, int -> str.'''
    tentativas = -1 
    inicio = 0
    if str.count (frase,letra) >= ocorrencia:
        while tentativas != ocorrencia:
            ondeEsta = str.find (frase, letra, inicio)
            if ondeEsta == 0:
                ondeEsta = 1
            inicio = inicio + ondeEsta 
            tentativas = tentativas + 1
        return ondeEsta
    else:
        return -1