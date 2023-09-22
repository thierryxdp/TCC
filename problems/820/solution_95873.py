def posLetra(string, letra, n):
    """Função que retorna a letra pedida input str, str, int, return int or str"""
    indice = ocorrencia = 0
    while indice < len(string):
        if string[indice] == letra:
            ocorrencia += 1
            if ocorrencia == n:
                return string.index(string[indice], indice)
        indice += 1
    else:
        return -1