def posLetra(string, letra, num):
    """Dada uma string uma letra e um numero que
    corresponde a ocorrencia da letra, calcula a
    posição desta ocorrência. str, str, int -> int """
    i = 0
    while i < (num + 1):
        if num <= str.count(string, letra) and num == 1:
            ocorrencia = str.index(string, letra)
            return ocorrencia
        elif num <= str.count(string, letra):
            ocorrencia = str.index(string, letra)
            ocorrencia = ocorrencia + 6
            resp = str.index(string, letra, ocorrencia)
        else:
            return -1
    i = i + 1
    return resp