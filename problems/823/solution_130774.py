def faltante(lista):
    contador = 0
    contador2 = 1 
    while contador < len(lista) + 1:
        if contador == len(lista):
            return len(lista) + 1
        if lista[contador] != contador2:
            return contador2
        contador = contador + 1
        contador2 = contador2 + 1