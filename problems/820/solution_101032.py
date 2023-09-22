def posLetra(string,letra,n):
    """retorna em que posição da string a ocorrência n da letra está.
    str,str,int->int"""
    pos = string.find(letra)
    while pos >= 0 and n > 1:
        pos = string.find(letra, pos + 1)
        n -= 1
    return pos