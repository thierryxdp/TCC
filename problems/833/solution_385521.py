def conta_numero(num,matriz):
    """funcao que dado uma matriz de inteiros de tamanho qualquer e um numero inteiro,retorna quantas vezes o numero aparece na matriz;
       list,int->int"""
    repeticoes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            repeticoes=repeticoes+1
    return repeticoes