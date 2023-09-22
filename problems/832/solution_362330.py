def eh_quadrada (matriz):
    
    ''' Função que identifica se matriz
        é quadrada.
        list -> bool '''
    
    resposta = False
    
    if matriz == []:
        resposta = True
    else:
        for l in matriz:
        	for c in matriz[l]:
            	if l == c:
                	resposta = True
                else:
                    resposta = False