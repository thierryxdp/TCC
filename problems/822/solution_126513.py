def repetidos(lista):
    ''' Função que conta quantas vezes o numero se repetiu em caso do numero antecessor for ele mesmo.
    list, int -> int'''
    i = 0
    contador = 0
    resultado = 0
    while contador < len(lista):
        if lista[i] == lista[i - 1]:
            resultado = resultado + 1

        i = i + 1
        contador = contador + 1

    return resultado