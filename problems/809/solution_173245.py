def intercala(lista1:list, lista2:list)->list:
    """Dadas duas listas com 3 posições, retorna uma outra lista que possui seis posições, e é originada intercalando as posições das listas, com a posição 1 com a 1, 2 com a 2 e 3 com a 3"""
    return list(lista1[0]) + list(lista2[0]) + list(lista1[1]) + list(lista2[1]) + list(lista1[2]) + list(lista2[2])