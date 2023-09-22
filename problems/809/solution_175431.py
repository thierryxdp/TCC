def intercala(lista1, lista2):
    """
    Função que dada duas listas,L1 e L2, de tamanho 3,
    gera uma lista L3 que é formada intercalando os elementos
    de L1 e L2.
    Parametro de Entrada:list
    Valor de Saida:list
    """
    L_3=lista1+lista2
    
    L_3[1]=lista2[0]
    L_3[2]=lista1[1]
    L_3[3]=lista2[1]
    L_3[4]=lista1[2]