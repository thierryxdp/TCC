import re
def posLetra(string,letra,numero):
    """retorna em que posição da string a ocorrência da letra está
    caso não alcance a ocorrência pedida retorna -1;
    string, string, int -> int"""
    
    contar = 0
    while contar < len(string):
        if letra in string[contador]:
        contar = contar + 1
    return contar