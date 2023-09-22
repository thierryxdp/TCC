def faltante(lista_de_numeros):
    numero_inicial = lista_de_numeros[0]
    numero_final = lista_de_numeros[len(lista_de_numeros)-1]
    lista_correta = [1]
    numero = numero_inicial

    while lista_correta[len(lista_correta)-1] != numero_final:
        lista_correta.append(numero)
        numero += 1
    if numero_inicial == 1:
        lista_correta.pop(0)


    indice = 0
    for numero in lista_de_numeros:
        if lista_de_numeros[indice] != lista_correta[indice]:
            return numero - 1
        else:
            return numero_final + 1
        indice += 1