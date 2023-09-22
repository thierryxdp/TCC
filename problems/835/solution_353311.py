def melhor_volta(matriz):
    '''a funcao retorna qual corredor teve a melhor volta, em qual tempo e em qual volta
    list->tuple'''
    menor1=min(matriz[0])
    menor2=min(matriz[1])
    menor3=min(matriz[2])
    menor4=min(matriz[3])
    menor5=min(matriz[4])
    menor6=min(matriz[5])
    
    menores=[menor1,menor2,menor3,menor4,menor5,menor6]
    menor_valor=min(menores)
    
    for i in range(len(matriz)):
        if menor_valor in matriz[i]:
            lista=matriz[i]
            corredor=i+1
    volta=1+lista.index(menor_valor)

    return corredor,menor_valor,volta