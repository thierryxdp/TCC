def eh_quadrada(matriz):
    '''Função que retorna True caso a matriz seja quadrada e False se não for.
    list -> bool'''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
        
    if linhas == colunas or colunas == 0:
        return True
    else:
        return False