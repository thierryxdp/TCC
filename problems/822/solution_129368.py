def repetidos(lista):
    contador = 0
    for numero in lista:
        if numero == numero - 1:
            contador = contador + 1
    return contador