def conta_numero(numero,matriz):
    '''Recebe uma matriz de inteiros e conta quantas vezes o 'numero' aparece;
retornando tal valor;
int,list => int'''
    if len(matriz)==0:
        return 0
    else:
        y = len(matriz)
        x = len(matriz[0])
        i = 0
        n = 0
        conta = 0
        while i<y:
            while n<x:
                if matriz[i][n]==numero:
                    conta = conta+1
                n = n+1
            n = 0
            i = i+1
        return conta