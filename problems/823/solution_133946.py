def faltante(lista):
    ''''''
    contador = 0
    while contador < len(lista):
        if lista[contador] - contador != 1:
            return contador