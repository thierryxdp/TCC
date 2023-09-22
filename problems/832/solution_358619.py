def eh_quadrada(m):
    """Função que identifica se matriz é quadrada
    	list -> bool"""
    
   
    if m==[]:
    linhas = len(m)
    colunas = len(m[0])
        return True
    
    elif colunas!=linhas:
        return False
    else:
        return True