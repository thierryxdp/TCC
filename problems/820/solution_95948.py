def posLetra (string, letra, numero):
    """Recebe uma string, uma letra e um número e retorna a 
    posição da letra de acordo com a ocorrência desejada, 
    determinada pelo número dado.
    str, str, int -> int"""
    indice = 0
    posicao = []
    while indice < len(string):
        if string[indice] == letra:
            posicao += str.index (string[indice:], letra)
    indice += 1
    if len(posicao) > numero:
        return posicao[numero]
    else: 
        return -1