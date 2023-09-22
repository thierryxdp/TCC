def posLetra(string,letra,n):
    """retorna em que posição da string a ocorrência n da letra está.
    str,str,int->int"""
    pos = str.find(string,letra)
    while pos >= 0 and n > 1:
        pos = str.find(string,letra, pos + 1)
        n -= 1
    return pos