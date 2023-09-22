def conta_numero(numero,matriz):
    '''retorna a quantidade de vezes em que o número é
    encontrado;
    int,list(list(int))->int'''
    
    rep=0
    
    for i len(matriz):
        for j len(matriz[0]):
            if matriz[i][j]==numero:
                rep+=1
    return rep