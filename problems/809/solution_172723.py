def intercala(lista1,lista2):
    """Dada duas listas L1 e L2 com o tamanho 3, gera uma lista L3 que é formada intercalando os elementos da L1 e L2. Considere como paramêtro de entrada a lista1 [[1,2,4,16,32,64,-128] e de saída lista2 [3,5,17,33,65,-129]"""
    [*sum(zip(l2,l1),())]