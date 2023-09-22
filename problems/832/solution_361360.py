def eh_quadrada(matriz):
    #Funcao que retorna um valor booleano que indica se  a matriz inserida eh quadrada ou nao
    if matriz == []:
    	return True
    
    if len (matriz) == len (matriz[0]):
        return True
    
    else:
        return False