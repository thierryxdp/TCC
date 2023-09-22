def posLetra(string, letra, numero):
    '''retorna em que posição da string, aquela ocorrência da letra está
    str, str, int -> int'''
    indice = 0
    contador = 0
    ocorrencia = str.count(string, letra)
    if numero > ocorrencia:
        return -1
    else:
        return str.index(string, letra, numero)