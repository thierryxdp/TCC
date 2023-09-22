def posLetra(string, letra, numero):
    '''retorna em que posição da string, aquela ocorrência da letra está
    str, str, int -> int'''
    indice = 0
    contador = 0
    while indice < len(string):
        while contador < numero:
            if string[indice] == letra:
                indice = indice + 1
                contador = contador + 1
            else:
                indice + indice + 1
        indice = indice + 1
        if numero > str.count(string, letra):
            return -1
        else:
            return indice