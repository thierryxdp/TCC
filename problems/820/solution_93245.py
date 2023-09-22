def posLetra(string, letra, numero):
    '''retorna em que posição da string, aquela ocorrência da letra está
    str, str, int -> int'''
    indice = 0
    contador = 0
    while indice < len(frase):
        if string[indice] == letra:
            contador = contador + 1
            indice = indice + 1
            if contador == numero:
                return indice
        else:
            indice = indice + 1