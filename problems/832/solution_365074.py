def eh_quadrada(m):
   ''' função que identifica se a matriz é quadrada'''
    linha = len(m)
    coluna= len(m[0])
    for i in m:
        if linha== coluna:
            return True 
        else:
            return False