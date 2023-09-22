def intercala(lista1, lista2):
    """Retorna uma lista de tamanho 6 formada pela intercalação 
    dos elementos das listas 1 e 2 (de tamanho 3 cada) dadas
    como entrada.
    list, list -> list"""
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]