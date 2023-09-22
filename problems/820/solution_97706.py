def posLetra (string, letra, numero):
    """Função que retorna em que posição de uma frase se encontra uma ocorrencia recebida a partir de uma string, uma letra e um número indicando a ocorrencia da letra
    str, str, str -> int"""
    x = 0
    for y in range(len(string)):
        if (string[y] == letra):
            x = x + 1
        if (x == numero):
            return y
    return -1