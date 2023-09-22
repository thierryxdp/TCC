def eh_quadrada(matriz):
    
    '''Função que verifica se a matriz dada é quadrada,
    sendo também considerada quadrada uma matriz vazia.
    
    :param matriz:list
    :return:bool''''
    
    linhas=len(matriz)
    colunas=len(matriz[0])
    
    if linhas==colunas:
        return True
    else:
        return False