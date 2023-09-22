def conta_numero(numero,matriz):
    '''
    funcao que dado um numero int e uma matriz de int de tamanho qualquer, conta e retorna quantas vezes aquele numero
    aparece na raiz
    int,list->int
    '''
    con=0
    for n in range(len(matriz)):
        
        m=matriz[n]
        for k in range(len(m)):
            if m[k]==numero:
                con=con+1
            else:
                con
    return con