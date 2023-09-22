def faltante(lista):
    ''''''
    if 1 not in lista:
        return 1
    if 1 in lista:
        contador = 0
        while contador < len(lista):
            if abs(lista[contador] - contador) != 1:
                return contador - 1
            contador = contador + 1