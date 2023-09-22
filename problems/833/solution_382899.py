def conta_numero(num, matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros de qualquer
    tamanho, retorna quantas vezes esse número aparece na matriz.
    Entrada: int,list(list,list). Saída: int'''
    qtd_num=0
    for L in range(len(matriz)):
        for C in range(len(matriz[L])):
            if matriz[L][C]==num:
                       qtd_num=qtd_num+1
    return qtd_num