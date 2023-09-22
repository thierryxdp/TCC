def eh_quadrada(numero):
    '''Função para identificar se a matriz é quadrada, list -> bool'''
    linha = 1
    coluna = 0
    for i in range(len(numero)):
        linha = linha + 1
    	for j in range(len(numero[0])):
            if linha == 0:
                return True
    	    elif linha == coluna:
        	    return True
    	    else:
        	    return False
    else:
        return True