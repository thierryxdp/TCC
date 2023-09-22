def repetidos(lista):
    indice = 0
    contador = 0
    repeticao = 0
    while contador < len(lista):
        if lista[indice] == lista[indice - 1]:
            repeticao += 1

        indice += 1
        contador += 1

    return repeticao