def intercala(lista1, lista2):
    """Dado duas listas, lista1 e lista2, retorne uma nova lista intercalando os elementos;
    list,list -> list"""
    a=[*sum(zip(lista1,lista2),())]
    return a