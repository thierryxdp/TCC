def repetidos(lista):
    contador = 0
    n = 0
    while contador < len(lista)-1:
        if lista[contador+1] == lista[contador]:
            n = n + 1
        contador = contador + 1
    return n