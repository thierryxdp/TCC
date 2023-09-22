def colchao(medidas, H, L):
    """ Função que recebe as medidas de uma porta e de um colchão
    e verifica se o colchão passa ou nao pela porta.
    lista, inteiro, inteiro --> boolean """
    
    A, B, C = medidas
    if H >= A and L >= B or H >= A and L >= C or H >= B and L >= A or H >= B and L >= C and L >= B:
    	return True 
    else:
        return False