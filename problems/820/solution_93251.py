def posLetra(string, letra, numero):
    '''retorna em que posição da string, aquela ocorrência da letra está
    str, str, int -> int'''
    indice = 0
    contador = 0
    while contador < numero:
        if string[indice] == letra:
            indice = indice + 1
            contador = contador + 1
        else:
            indice + indice + 1
        return indice