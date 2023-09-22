def faltante(lista):
    ''''''
    if 1 not in lista:
        return 1
    else:
        contador = 0
        while contador < len(lista):
            if abs(lista[contador] - contador) != 1:
                return lista[contador]
            contador = contador + 1