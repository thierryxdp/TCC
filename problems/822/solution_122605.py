def repetidos(lista):
    '''Função que recebe uma lista de números e retorna quantas vezes um
    elemento da lista é igual ao elemento anterior. Na lista, pode conter
    números repetidos. Entrada: list. Saída: int'''
    contador = 1
    acumulador = 0
    while contador<len(lista):
        if lista[contador]==lista[contador-1]:
            acumulador = acumulador + 1
        contador=contador+1
    return acumulador