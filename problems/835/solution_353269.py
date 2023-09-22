def melhor_volta(matriz):
    '''a funcao retorna qual corredor teve o menor tempo, o tempo e em qual volta
    list->tuple'''
    corredor1=matriz[0]
    min_valor1=min(matriz[0])
    corredor2=matriz[1]
    min_valor2=min(matriz[1])
    corredor3=matriz[2]
    min_valor3=min(matriz[2])
    corredor4=matriz[3]
    min_valor4=min(matriz[3])
    corredor5=matriz[4]
    min_valor5=min(matriz[4])
    corredor6=matriz[5]
    min_valor6=min(matriz[5])
    
    lista_menores=[min_valor1,min_valor2,min_valor3,min_valor4,min_valor5,min_valor6]
    menor_valor=min(lista_menores)
    posicao=matriz.index(menor_valor)
    
    
    return (posicao,menor_valor)