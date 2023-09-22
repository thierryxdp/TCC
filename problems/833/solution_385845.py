def conta_numero(numero,matriz):
    '''retorna a quantidade de vezes que o numero aparece na matriz
    int,list->int'''
    
    ocorrencia=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):