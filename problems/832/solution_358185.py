def eh_quadrada(matriz):
    '''teste'''
    
    linhas=len(matriz)
    colunas=len(matriz[0])
    resultado=''
    
    if linhas==colunas:
        resultado=resultado+'True'
    else:
        resultado=resultado+'False'
            
    return resultado