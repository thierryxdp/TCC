def faltante(lista):
    ''''''
    
    contador = 0
    while contador < len(lista):
        if abs(lista[contador] - contador) != 1:
            return lista[contador]
        contador = contador + 1