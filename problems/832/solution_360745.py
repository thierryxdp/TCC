def eh_quadrada(matriz):
    ''' Entrada: matriz -> dado do tipo list
    	
        Saída: dado do tipo booleano o qual identifica se a matriz 
        	  dada é quadrada 
        
        list-> bool'''
    if len(matriz)==0 or len(matriz)==len(matriz[0]):
        return True
    else:
        return False