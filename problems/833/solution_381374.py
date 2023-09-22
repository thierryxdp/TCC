def contamatriz(numero,matriz):
    '''dado um numero inteiro e uma matriz de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na amtriz;int,lista->int'''
    contador=0
    for m in range(len(matriz)):
        for n in range(len(matriz[0])):
            if matriz[m][n]==numero:
                contador+=1
            else:
                contador+=0