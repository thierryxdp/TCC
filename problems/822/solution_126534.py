def repetidos(lista_numeros):
   
    proximo = 0
    numero = 0
    while proximo<len(lista_numeros):
        if lista_numeros[proximo - 1] == lista_numeros[proximo]:
            numero = numero + 1
        proximo = proximo + 1
    return numero