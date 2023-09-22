def conta_numero(n,m):
    '''Retorna a quantidade de vezes que o inteiro n de entrada aprece
       na matriz m, também de entrada;
       int, list -> int'''
    contaNumero=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==n:
                contaNumero+=1
    return contaNumero