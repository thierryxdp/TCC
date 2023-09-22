def eh_quadrada(m):
    """Função que identifica se matriz é quadrada
    	list -> bool"""
 	
    if m==[]:
        return True
    
    linhas = len(m) 
    colunas = len(m[0])
    
    if colunas!=linhas:
        return False
    
    else:
        return True