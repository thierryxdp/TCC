def posLetra(string, letra, numero):
    '''retorna em que posição da string, aquela ocorrência da letra está
    str, str, int -> int'''
    indice = 0
    contador = 0
    ocorrencia = str.count(string, letra, numero)
    while indice < len(string):
        if ocorrencia < numero:
            return -1
        else:
            if string[indice] != letra:
                indice = indice + 1
            else:
                indice = indice + 1
                contador = contador + 1
                if contador == numero:
                    return str.index(string, letra, numero)