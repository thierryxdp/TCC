def repetidos(lista):
    contador= 0
    acomulador = 0
    while contador < len(lista) - 1:
        if lista[contador + 1] == lista[contador]:
            acomulador = acomulador+ 1
            contador = contador + 1
        elif lista[contador + 1] != lista[contador]:
            contador = contador + 1
    return acomulador