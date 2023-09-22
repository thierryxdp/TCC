def intercala(lista1,lista2):
    """funcao que dada duas listas retorna uma teceira lista com os elementos intercalados"""
    return [*sum(zip(lista1,lista2),())]