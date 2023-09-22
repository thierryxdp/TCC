def posLetra(string, letra, numero):
    '''retorna a posição em que posição da astring aquela ocorrência da letra está
    string, string, int -> int'''
    indice = 0
    contador = 0
    while indice < len(string):
        indice = indice + 1
        if string[indice] != letra:
            indice = indice + 1
        else:
            indice = indice + 1
            contador = contador + 1
            if contador == numero:
                return indice - 1
            else:
                return -1