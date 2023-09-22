def eh_quadrada(matriz):
    '''Função que retorna True caso a matriz seja quadrada e False se não for.
    list -> bool'''
    
    linhas = len(matriz)
    
    if linhas == 0:
        return True
    
    colunas = len(matriz[0])
        
    if linhas == colunas:
        return True
    else:
        return False