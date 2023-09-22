def faltante(lista):
    contador = 0
    contador2 = 1 
    while contador < len(lista) + 1:
        if lista[contador] != contador2:
            return lista[contador]
        contador = contador + 1
        contador2 = contador2 + 1