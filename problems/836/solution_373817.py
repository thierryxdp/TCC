def busca(setor,matriz):
    '''A função buscará as informações dos funcionários de um determinado setor
    Dados de entrada -> string, lista
    Dados de saída -> lista'''
    
    nlinha = len(matriz)
    ncoluna = len(matriz[0])
    resultado = []
    
    for i in range(nlinha):
        if setor == matriz[i][2]:
            resultado += [[matriz[i][0],matriz[i][1],matriz[i][3]]]
            
    return resultado