def posLetra(frase, letra, n):
    '''Retorna em que posição da frase a ocorrência n da letra está, str, str, int -> int'''
    posicao=str.find(frase,letra)
    while posicao>=0 and n>1:
        posicao=str.find(frase,letra, posicao+1)
        n = n-1
    return posicao