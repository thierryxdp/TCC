def posLetra (string, letra, numero):
    """Recebe uma string, uma letra e um número e retorna
    a posição da repetição da letra de acordo com o número 
    escolhido.
    str, str, int -> int"""
    indice = 0
    posicao = []
    while indice < len(string):
        if string[indice] == letra:
            posicao += str.find(string[indice:], letra)
    indice += 1
    return posicao[numero] or -1