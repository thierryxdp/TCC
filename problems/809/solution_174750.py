def intercala(lista1, lista2):
    """A função irá intercalar os dados de duas lista (lista1 e lista2) em uma terceira lista.
    Cada lista poderá admitir apenas 3 elementos
    
    Exemplo: lista1 = [1,3,5] e lista2 = [2,4,6] gera lista3 = [1,2,3,4,5,6]
    
    dados de entrada -> list, list
    dados de saída -> list"""
    
    L1_1 = lista1[0]
    L1_2 = lista1[1]
    L1_3 = lista1[2]
    
    L2_1 = lista2[0]
    L2_2 = lista2[1]
    L2_3 = lista2[2]
    
    lista3 = [L1_1, L2_1, L1_2, L2_2, L1_3, L2_3]
    
    return lista3