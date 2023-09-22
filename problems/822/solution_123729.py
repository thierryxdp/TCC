repetido(lista_numeros):
    lista= lista_numeros
    contador = 0
    contador2 = 1
    while contador <len(lista):
        if lista[contador] == lista[contador2]:
            contador = contador +1
            contador2 = contador +1
    return contador2