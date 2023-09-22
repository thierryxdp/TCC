def qtd_divisores(numero):
    ''' Entrada: numero -> dodo do tipo int
    	
        Saída: Divisores -> numero de divisores que o numero 
        	  de entrada possui, dado do tipo int
        
        int -> int'''
    divisores = 0
    for x in range(1,numero+1):
        if numero%x == 0:
            divisores = divisores + 1
    return divisores