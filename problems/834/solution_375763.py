def media_matriz(matriz):
    '''media_matriz recebe uma matriz e devolve um numero inteiro
    determine a media de todos os numeros das matrizes
    list(list) --> int'''
    
    todosn=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]:
                list.append(todosn,matriz[i][j])
            else:
                list.append(todosn,matriz[i][j])
                
    resposta=sum(todosn)/len(todosn)
                
    return round(resposta,2)