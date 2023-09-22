def melhor_volta(matriz):
    '''a funcao retorna qual corredor teve a melhor volta, em qual tempo e em qual volta
    list->tuple'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            menor_valor=menor_valor+min(matriz[i][j])
    
    return menor_valor