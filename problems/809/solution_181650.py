def intercala(lista1, lista2):
    """Dada as listas L1 e L2, gera uma lista L3 que é formada intercalando os elementos de L1 e L2
    assinatura: list (int, int, int), list (int, int, int) ->  list (int, int, int, int, int, int)
    testes:
    intercala(
    """
    return [lista1[0] , lista2[0] , lista1[1] , lista2[1] , lista1[2] , lista2[2]]