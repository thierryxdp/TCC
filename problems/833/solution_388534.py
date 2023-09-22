def conta_numero(numero,matriz):
    '''função que recebe uma matriz e um número e retorna quantas vezes esse número aparece na matriz
    list,int->int'''
    
    vezes=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                vezes=vezes+1
                
    return vezes