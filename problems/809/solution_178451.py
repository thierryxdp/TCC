def intercala (lista1, lista2):
    """dadas duas listas como parametro, lista1 e lista2 gera uma outra lista com ambas restectivamente intercaladas."""
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]