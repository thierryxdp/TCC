def repetidos (lista):
    contador = 0
    vezes = 0
    while contador < len(lista):
        if lista[contador] == lista[contador-1]:
            vezes = vezes+1
        else:
            vezes = vezes+contador
        contador = contador + 1
        return vezes