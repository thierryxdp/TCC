def posLetra(string,letra,ocorrencia):
    ''' Função que recebe uma string, uma substring(letra) e o numero
    da ocorrencia (1°,2°) da substring e retorna em que posição da string
    está a letra de acordo com sua ocorrencia. Se as ocorrencias forem menor
    do que a ocorrencia da entrada, retorna -1. Entrada: str,str,int.
    Saída:int'''
    indice=0
    contador=0
    
    while indice<len(string):
        if string[indice]==letra:
            contador=contador+1
        if contador==ocorrencia:
            return indice
        indice+=1
    
    return -1