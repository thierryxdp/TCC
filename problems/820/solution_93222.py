def posLetra(string, letra, numero):
    '''retorna em que posição da string, aquela ocorrência da letra está
    str, str, int -> int'''
    indice = 0
    contador = 0
    ocorrencia = str.count(string, letra)
    while indice < len(string):
        if numero <= ocorrencia:
            if string[indice] == letra:
                contador = contador + 1
                indice = indice + 1
            indice = indice + 1
        else:
            return -1
        return contador