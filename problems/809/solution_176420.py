def intercala(L1, L2):
    """
    retorna uma lista que intercala os elementos das
    listas L1 e L2
    
    espera-se que as listas L1 e L2 possuam três
    elementos cada
    
    list, list -> list
    """
    L3 = L1[1] + L2[1] + L1[2] + L2[2] + L1[3] + L2[3]
    return L3