# A funçao tera duas linhas l1 e l2 de tamanho 3 e gera uma lista l3 em formato intercalado os elementos l1,l2
#lista1,lista2
def intercala(lista1, lista2):
    """Funçao que, dado duas lista L1 e L2  de tamanho 3,
        gera uma terceira lista L3 que é formada pela
        intercalação dos elementos das listas L1 e L2.
        list (int), list (int)-> list (int)"""
    A = lista1[0] , lista2[0] ,lista1[1]
    B = lista2[1] , lista1[2] , lista2[2]
    return list(A)+list(B)