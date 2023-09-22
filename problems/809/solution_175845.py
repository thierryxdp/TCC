def intercala(lista1, lista2):
    """Recebe duas listas L1 e L2 de tamanho 3 as duas e 
    retorna uma L3 que é formada intercalando as listas 1 e 2;
    list -> list"""
    L3=[lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]
    return L3