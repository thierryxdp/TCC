def conta_numero(n,matriz):
    ''' Função que conta quantas vezes o numero se repete nesta lista, quando existir.
int,list -> int'''
    qnt = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == n:
                qnt += 1
    return qnt