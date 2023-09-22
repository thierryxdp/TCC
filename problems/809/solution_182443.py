def intercala(lista1, lista2):
    """
    Dada duas listas de tamanho 3, a função 
    gera uma outra lista que é formada intercalando
    os elementos da lista 1 e lista 2. 
    list, list --> list
    """
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]