def conta_numero(numero,matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer,
    conta e retorna quantas vezes aquele número aparece na matriz;
    Entrada: int,list(int)
    Saída: int'''
    contador = 0
    if matriz==[]:
        return 0
    else:
        linha=len(matriz)
        coluna=len(matriz[0])
        for i in range(linha):
            for j in range(coluna):
                if matriz[i][j]==numero:
                    contador = contador+1
    return contador