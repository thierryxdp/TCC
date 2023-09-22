def conta_numero(numero,matriz):
    '''Funcao que recebe um numero inteiro e uma matriz de
       inteiros de tamanho qualquer, conta e retorna quantas 
       vezes aquele número aparece na matriz.
       : param numero: int
       : param matriz: list
       : return: int
     '''
    qtd_vezes=0
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            for numero in len(matriz):
                if numero in matriz:
                    qtd_vezes+=matriz.count(numero)
    return qtd_vezes