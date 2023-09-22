def posLetra(texto, letra, n):
    '''Retorna em que posição da string aquela ocorrência da letra está
    str, str, int -> int'''
    if list(texto).count(letra)>=n:
        return str.find(str.replace(texto,letra,'n'))
    else:
        return -1