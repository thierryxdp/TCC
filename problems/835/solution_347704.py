def melhor_volta(matriz):
    '''funcao retorna a melhor volta e o piloto que a realizou. list->tupla'''
    count=[]
    for i in range(1,len(matriz)):
        for j in range(len(matriz[i])):
            count.append(matriz[i][j])
            if min(count)==matriz[i][j]:
                c=matriz[0][j]
    return min(count),c