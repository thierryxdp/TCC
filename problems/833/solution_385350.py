def conta_numero(numero,matriz):
    '''Função que conta e retorna quantas vezes o numero
    inteiro dado aparece na matriz dada de tamanho qualquer.
    int, list ->int'''
    ocorrencia=0
    total=0
    for i in range(len(matriz)):
        n=0
        for j in range(len(matriz[i])):
            total=total+1
            if matriz[i][j]==numero:
                ocorrencia=ocorrencia+1
    return ocorrencia