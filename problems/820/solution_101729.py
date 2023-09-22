def posLetra(string,letra,ocorrencia):
    """retorna em que posição da string a ocorrência está
    str,str,int -> int"""
    pos = 0
    contador = 0
    while pos < len(string):
        if string[pos] == letra:
            contador = contador + 1
            if contador == ocorrencia:
                return pos
        pos = pos + 1
    return -1