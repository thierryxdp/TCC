def conta_numero(matriz,n):
    """Calcula e retorna quantas vezes o número inteiro dado aparece na
       matriz dada;
       list,int->int
       Parâmetros:
       matriz: matriz composta por números inteiros
       n: número inteiro 
    """
    contador=0
    for i in range(len(matriz)):
        for num in range(len(matriz[i])):
            elemento=matriz[i][num]
            if elemento==n:
                contador=contador+1
    return contador