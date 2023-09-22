def repetidos(lista):
    """funcao que recebe uma lista como entrada e retorna o numero de vezes que um elemento da lista é igual ao elemento anteriro
    list -> int"""
    contador = 0
    acumulador = 0
    while contador < len(lista) -1:
        if lista[contador + 1] == lista[contador]:
            acumulador = acumulador + 1
            contador = contador + 1
            elif losta[contador + 1] != lista[contador]:
                contador = contador + 1
    return acumulador