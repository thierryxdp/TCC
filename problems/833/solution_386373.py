def conta_numero(numero,matriz):
    '''
    	Função que recebe um número 
        inteiro e uma matriz de 
        inteiros, e retorna quantas 
        vezes esse número aparece na
        matriz
        : param numero: int
        : param matriz: list(list)
        : return: int
    '''
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    quantas_vzs_aparece = 0
    
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            if matriz[linha][coluna] == numero:
                quantas_vzs_aparece += 1
    
    return quantas_vzs_aparece