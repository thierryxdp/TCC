def posLetra(frase:str, letra:str, n:int):
    '''recebe uma string, letra e número que indica a ocorrência
       desejada da letra, a função retorna em que posição da string
       aquela ocorrência de letra está'''
    pos = frase.find(letra)
    while pos >= 0 and n > 1:
        pos = frase.find(letra, pos + 1)
        n -= 1
    return pos