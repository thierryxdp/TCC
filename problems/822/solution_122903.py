def repetidos(lista_numeros):
    contador = 0
    vezes = 0
    while contador < len(lista_numeros)-1:
        if lista_numeros[contador + 1] == lista_numeros[contador]:
       		 vezes = vezes + 1
    return vezes