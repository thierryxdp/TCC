def conta_numero(numero,matriz):
    '''Funcao que recebe um numero inteiro e uma matriz de
       inteiros de tamanho qualquer, conta e retorna quantas 
       vezes aquele número aparece na matriz.
       : param numero: int
       : param matriz: list
       : return: int
     '''
    qtd_vezes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero==matriz[i][j]:
                qtd_vezes+=1
    return qtd_vezes