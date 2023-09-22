def posLetra(frase,letra,numero):
    '''
    dado uma str, ume letra e um numero que indicara a
    quantidade de ocorrencias da letra desejada, retorna
    posição a n-ésima repeticao da letra informada nar str
    dados de entrada: str, str, int
    retorna: int
    '''
    if numero > str.count(frase,letra):
        return -1
    contador = 0
    repeticao = 0
    while repeticao == numero:
        if frase[contador] == letra:
            repeticao = repeticao + 1
        contador = contador + 1
    return contador - 1