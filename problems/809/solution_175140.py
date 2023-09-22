def intercala(lista1, lista2):
    """Dadas duas listas de tamanho 3, gera uma lista com a juncao intercalada das duas fornecidas;
    list, list -> list"""
    
    pos1 = lista1[0]
    pos2 = lista2[0]
    pos3 = lista1[1]
    pos4 = lista2[1]
    pos5 = lista1[2]
    pos6 = lista2[2]
    
    return [pos1, pos2, pos3, pos4, pos5, pos6]