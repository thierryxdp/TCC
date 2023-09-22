def fatorial(numero):
    
   '''
   funcao que dado um numero calcula o seu fatorial
   float -> float
   '''

	contador = 0
    
    while numero > 0:
    	contador = contador + numero*numero-1
    numero = numero - 1
        
    return contador