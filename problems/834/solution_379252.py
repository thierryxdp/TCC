def media_matriz(matriz):
    '''
    	Função que recebe uma matriz
        como parâmetro de entrada, e
        retorna a média de todos os 
        números da matriz
        : param matriz: list(list)
        : return: float
    '''
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    soma_dos_num = 0
    qtd_num = num_linhas*num_colunas
    
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            soma_dos_num += matriz[linha][coluna]
    media = soma_dos_num/qtd_num
    
    return round(media,2)