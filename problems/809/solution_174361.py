def intercala(lista1, lista2):
    """Funcao retorna os elementos das listas: lista1 e lista2 intercalados
    OBS: As listas devem ter no maximo 3 elementos """
    
    l3 = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]

    caso1 = len(lista1) != 3
    caso2 = len(lista2) != 3
    
    if caso1 and caso2:
        return "Sua lista tem mais ou menos do que 3 elementos"
    else:
        return l3