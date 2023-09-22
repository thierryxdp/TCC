def lista_unica(lista):
    result = []
    for item in lista:
        if (isinstance(item, (list, tuple))):
            result = lista.extend(item)
        else:
            result.append(item)
    return result
def conta_numero(numero,matriz):
    matriz=lista_unica(matriz)
    repeticoes= matriz.count(numero)
    return repeticoes