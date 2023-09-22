def posLetra (frase, letra, ocorrencia):
    '''Função retorna em qual índice de posição da ocorrência da letra está na string. 
    str, str, int -> str.'''
    tentativas = 0 
    if str.count (frase, letra) >= ocorrencia:
        while tentivas != ocorrencia:
            ondeEsta = str.find (frase, letra)
    return ondeEsta