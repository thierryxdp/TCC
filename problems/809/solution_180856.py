def intercala(lista1, lista2):
    """Essa função gera uma lista 'L3' que ́e formada intercalando
    os elementos de 'L1' e 'L2'.
    Parametro de Entrada: list, list
    Valor de Retorno: list
    """
    L3=lista1+lista2
    L3[0]= lista1[0]
    L3[1]= lista2[0]
    L3[2]= lista1[1]
    L3[3]= lista2[1]
    L3[4]= lista1[2]
    L3[5]= lista2[2]
    return L3