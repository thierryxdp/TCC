def filtraMultiplos(lista_numeros, n):
    '''Função que recebe uma lista de números
    e um número n, e retorna outra lista com
    todos os elementos da lista de números 
    inicial que forem divisíveis pelo n.
    Dados de entrada: list, int
    Valor de saída: list
    '''
    indice_lista_numeros = 0
    lista_divisiveis_por_n = []
    while indice_lista_numeros < len(lista_numeros):
        if lista_numeros[indice_lista_numeros] % n == 0:
            lista_divisiveis_por_n.append(lista_numeros[indice_lista_numeros])
        indice_lista_numeros = indice_lista_numeros + 1
    return lista_divisiveis_por_n