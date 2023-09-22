def faltante(lista):
    """retorna o número que está faltando entre um intervalo N -1 
    list-> int"""
    contador = 0
    listaOrdenada = sorted(lista)

    while contador < len(lista):
        if contador + 1 == listaOrdenada[contador]:
            contador += 1

        else:
            return contador + 1

    return contador + 1