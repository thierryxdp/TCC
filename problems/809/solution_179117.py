def intercala(lista1, lista2):
    """função que dadas duas listas, retorna uma terceira com os valores intercalados das anteriores; list,list-> list"""
    return [lista1[0],]+[lista2[0],]+[lista1[1],]+[lista2[1],]+[lista1[2],]+[lista2[2],]