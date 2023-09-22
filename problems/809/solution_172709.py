def intercala(lista1,lista2):
    """ Essa função retorna uma lista que é composta por duas listas de tamanho 3
    intercaladas. Como entrada temos duas listas que contém números inteiros e
    retorna uma lista intercalando os números presentes nas duas listas"""
    L1= lista1
    L2= lista2
    L3=[L1[0],L2[0],L1[1],L2[1],L1[2],L2[2]]
    return L3