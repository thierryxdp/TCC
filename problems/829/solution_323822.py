def soma_h (numero):
    '''função que realiza a soma de frações de numerador 1 e 
    que o denominador, a cada fração soma + 1 até chegar ao valor dado
    int -> float'''
    
    contador =0
    
    for denominador in range (numero+1):
        if denominador != 0:
        	contador += 1/denominador
        
    return contador