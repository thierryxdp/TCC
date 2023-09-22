def conta_numero(numero,matriz):
    '''Função que retorna quantas vezes o numero dado aparece na matriz.
    int,list->int'''
    
    ocorrencia=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                ocorrencia+=1
    return ocorrencia