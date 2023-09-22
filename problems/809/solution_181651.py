def intercala(lista1, lista2):
    """Dada as listas L1 e L2, gera uma lista L3 que é formada intercalando os elementos de L1 e L2
    assinatura: list (int, int, int), list (int, int, int) ->  list (int, int, int, int, int, int)
    testes:
    intercala ([6, 2, 7], [5, 9, 1] == [6, 5, 2, 9, 7, 1]
    intercala ([4, 2, 3], [6, 2, 5]) == [4, 6, 2, 2, 3, 5]
    """
    return [lista1[0] , lista2[0] , lista1[1] , lista2[1] , lista1[2] , lista2[2]]