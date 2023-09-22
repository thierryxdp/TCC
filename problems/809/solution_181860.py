def intercala(lista1, lista2):
    """Intercalando os elementos de L1 e L2, listas de tamanho 3, gera-se uma lista L3.
    Assinatura: list, list ->  list #Apenas inteiros
    Casos de teste:
    intercala ([3, 5, 7], [4, 2, 1] == [3, 4, 5, 2, 7, 1]
    intercala ([7, 2, 5], [3, 2, 8]) == [7, 3, 2, 2, 5, 8]
    """
    return [lista1[0] , lista2[0] , lista1[1] , lista2[1] , lista1[2] , lista2[2]]