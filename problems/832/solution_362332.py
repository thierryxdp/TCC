def eh_quadrada (matriz):
    
    ''' Função que identifica se matriz
        é quadrada.
        list -> bool '''

    resposta = False
    
    if matriz == []:
        resposta = True
    
    else:
        for l in matriz:
            qtd_linhas = range(len(matriz))
            qtd_colunas = range(len(l))
            
            if qtd_linhas == qtd_colunas:
                resposta = True
                
    return resposta