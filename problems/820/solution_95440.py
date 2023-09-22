def posLetra(frase, letra, ocorrencia):
    '''Funcao que recebe uma string, letra e um numero que indica a ocorrencia desejada da letra.
    E retorna em que posicao da string aquela ocorrencia da letra esta.
    str, str, int -> int'''
    
    i = 0
    frase = list(frase)
    
    while i < len(frase):
        if frase[i] == letra:
            ocorrencia -= 1
        if ocorrencia == 0:
            return i
        i += 1
        
    return -1