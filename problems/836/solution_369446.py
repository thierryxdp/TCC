def busca(parte,matriz):
    '''retorna as informacoes dos funcionarios do setor 
    pesquisado no 1 arg
    str, list(list) -> list'''
    
    retorno = []
    n_linha = len(matriz)
    
    for i in range(n_linha):
        if parte == matriz[i][2]:
            retorno = retorno + [[matriz[i][0],matriz[i][1],matriz[i][3]]]
            
    return retorno