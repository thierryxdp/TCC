def conta_numero(numero,matriz):
    '''Dado um número e uma matriz, a função deve retornar
    quantas vezes aquele número aparece na matriz;
    int, list(list)->int'''
    
    quant_do_num_na_matriz=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(matriz[i][j]==numero):
                quant_do_num_na_matriz+=1
                
    return (quant_do_num_na_matriz)