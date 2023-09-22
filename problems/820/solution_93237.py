def posLetra(string, letra, numero):
    '''retorna em que posição da string, aquela ocorrência da letra está
    str, str, int -> int'''
    indice = 0
    contador = 0
    ocorrencia = str.count(string, letra)
    while contador < numero:
        if numero <= ocorrencia:
            indice = indice + 1
            contador = contador + 1
            return str.index(string, letra, numero)
        else:
            return -1