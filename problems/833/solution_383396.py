def conta_numero(numero,matriz):
    """
    int, lista -> int
    :param numero: Recebe um numero inteiro 
    :param matriz: Reeebe uma matriz de inteiros
    :param return: Retorna a quantidade de vezes o numero aparece na
    matriz. 
    """
    soma_numero = 0
    quantidade_de_linhas = range(len(matriz))
    quantidade_de_colunas = range(len(matriz[0]))
    for linha_da_matriz in quantidade_de_linhas:
        for posicao_da_coluna in quantidade_de_colunas:
            if numero == matriz[linha_da_matriz][posicao_da_coluna] and numero !=0:
                soma_numero +=1
    return soma_numero