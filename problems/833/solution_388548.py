def conta_numero(numero,matriz):
    '''Função que recebe um número e uma matriz e retorna quantas vezes 
    esse número aparece na matriz
    
    list,int->int'''
    
    qntd_vezes=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                qntd_vezes = qntd_vezes + 1
                
    return qntd_vezes