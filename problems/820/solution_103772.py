def posLetra(string, letra, ocorrencia):
    """Função que recebe como entrada uma string, uma letra,
    e um número que indica a ocorrência desejada da letra, e
    retorna em que posição da string aquela ocorrência da
    letra está;
    str, str, int -> int"""
    k = 0
    quantidade_letra = str.count(string, letra)
    indice = -1
    if quantidade_letra < ocorrencia:
        return -1
    elif quantidade_letra > ocorrencia:
        while k < ocorrencia:
            indice = str.index(string, letra, indice + 1, len(string))
            k = k + 1
        return  indice
    else:
        return str.index(string, letra)