def busca(setor,matriz):
    '''
    	Função que recebe um setor de 
        uma empresa e uma matriz com as 
        informações dos funcionários 
        dessa empresa, e retorna as 
        informações dos funcionários
        do setor dado como entrada
        : param setor: str
        : param matriz: list(list)
        : return: list(list)
    '''
    num_linhas = len(matriz)
    informacoes_setor = []
    
    for linha in range(num_linhas):
        if matriz[linha][2] == setor:
            list.append(informacoes_setor,
            del matriz[linha][2]