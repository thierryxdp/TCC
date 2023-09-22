def posLetra (texto, letra, numero_ocorrencia) :
    """Funcao que recebe uma mensagem de string, uma letra e um numero de ocorrencia e retorna em que posição da string aquele numero de ocorrencia esta"""
    contador = 0
    x = 0
    while contador < len(texto) and x < numero_ocorrencia:
        if texto[contador] == letra:
            x = x + 1
        contador = contador + 1
    if x < numero_ocorrencia:
        return -1
    else:
        return contador - 1