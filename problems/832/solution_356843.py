def eh_quadrada(matriz):
    """Função que retorna informando se a matriz passada é
    quadrada ou não.
    Entrada:list;
    Saida: bool;
    
    Parameters:
    matriz: lista com as listas que formam a matriz"""
    if matriz == []:
        return True
    else:
    	linhas = len(matriz)
    	colunas = len(matriz[0])
        
    	if linhas == colunas:
        	return True
    	else:
        	return False