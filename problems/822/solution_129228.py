def repetidos(lista):
    repetido = 0
    contador = 0
    while contador < len(lista):
        if l[contador] == l[contador-1]:
            repetido += 1
            contador += 1
        else:
            contador += 1
    return repetido