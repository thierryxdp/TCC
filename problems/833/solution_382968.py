def conta_numero(numero,matriz):
    '''Funcao que dada uma matriz
    de inteiros, nao vazia, de tamanho
    qualquer, conta e retorna quantas 
    vezes o dado numero aparece na matriz.
    Dados de entrada: int, list[list]
    Valor de saida: int 
    '''
    qtd_repeticoes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                qtd += 1
    return qtd_repeticoes