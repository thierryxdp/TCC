def eh_quadrada(m):
    """Função que identifica se matriz é quadrada
    	list -> bool"""
    linhas = len(m)
    colunas = len(m[0])
    
   
    if m=[]:
        return True
    
    elif colunas!=linhas:
        return False
    else:
        return True