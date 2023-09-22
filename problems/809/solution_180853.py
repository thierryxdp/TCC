def intercala(lista1, lista2):
    """Essa função gera uma lista 'L3' que ́e formada intercalando
    os elementos de 'L1' e 'L2'.
    Parametro de Entrada: list, list
    Valor de Retorno: list
    """
    L1=lista1
    L2=lista2
    L3=[]
    L3[0]= L1[0]
    L3[1]= L2[0]
    L3[2]= L1[1]
    L3[3]= L2[1]
    L3[4]= L1[2]
    L3[5]= L2[2]
    return L3