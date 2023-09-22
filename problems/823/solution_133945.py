def faltante(lista):
    ''''''
    contador = 0
    while contador < len(lista):
        if contador - lista[contador] != 1:
            return contador