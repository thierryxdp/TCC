def posLetra(string, letra, numero):
    '''retorna a posição em que posição da astring aquela ocorrência da letra está
    string, string, int -> int'''
    idice = 0
    while indice < len(string):
        if letra in string:
            return str.index(string, letra, numero)
        else:
            return -1