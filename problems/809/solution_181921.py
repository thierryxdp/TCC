def intercala(lista1, lista2):
    """função que intercala os elementos da lista 1 e lista 2 formando uma terceira lista sendo intercalado"""
    intercalada=[lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista2[1]]+[lista2[2]]
    if len(lista1)==3 or len(lista2)==3:
    return intercalada			
    else:
        """Está função trabalha somente com 3 elementos"""