def filtraMultiplos(lista_numeros,numero):
    '''
    dada uma lista de numeros e um numero, retorna uma
    lista com es elementos da lista inicial que são 
    divisiveis pelo numero fornecido
    dados de entrada: list, float
    retorna: list
    '''
    contador = 0
    acumulador = []
    while contador < len(lista_numeros):
        if lista_numeros[contador] % numero == 0:
            list.append(acumulador, lista_numeros[contador])
        contador = contador + 1
    return acumulador