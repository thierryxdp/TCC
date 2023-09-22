def posLetra(frase:str, letra:str, n:int) -> int:
    '''Recebe uma string, uma letra e um número, e retorna a posição do
    número de ocorrência (n) da letra desejada.'''
    i = 0
    pos = -1
    while i < n:
        pos = frase.find(letra, pos+1)
        i = i+1
        
    return pos