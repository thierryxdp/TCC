def intercala(lista1, lista2):
    """Dadas duas listas L1 e L2 de tamanho 3, gera uma 
    lista L3 que é formada intercalando os elementos de
    L1 e L2. list,list -> list """
    
    lista3 = lista1 + lista2
    lista3.sort()
    
    return lista3