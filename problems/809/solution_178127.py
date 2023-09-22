def intercala(L1, L2):
    """
    Recebe duas listas (L1 e L2). Cria uma terceira lista.
    Adiciona em L3, os valores de L1 e L2 de forma intercalada.
    list, list ->  list
    """
    L3 = []
    L3.append(L1[0])
    L3.append(L2[0])
    L3.append(L1[1])
    L3.append(L2[1])
    L3.append(L1[2])
    L3.append(L2[2])
    return L3