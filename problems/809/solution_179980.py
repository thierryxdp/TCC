def intercala(lista1, lista2):
    """Funcao que dadas 2 listas de tamanho 3, gera uma terceira lista
    formada intercalando os elementos de lista1 e lista2
    list, list -> list"""
    
    a, c, e = lista1
    b, d, f = lista2
    lista3 = [a, b, c, d, e, f]
    
    return lista3