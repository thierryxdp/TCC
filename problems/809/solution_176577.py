def intercala(lista1, lista2):
    """funcao que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que e formada intercalando os elementos de L1 e L2;
    lista, lista-> lista"""
    L1= lista1
    L2= lista2
    return L1[0:1]+L2[0:1]+L1[1:2]+L2[1:2]+L1[2:]+L2[2:]