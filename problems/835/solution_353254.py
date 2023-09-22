def melhor_volta(matriz):
    '''a funcao retorna qual corredor teve o menor tempo, o tempo e em qual volta
    list->tuple'''
    corredor1=matriz[0]
    corredor2=matriz[1]
    corredor3=matriz[2]
    corredor4=matriz[3]
    corredor5=matriz[4]
    corredor6=matriz[5]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            menor_valor=min(min(matriz[i][j]))
          
    return menor_valor