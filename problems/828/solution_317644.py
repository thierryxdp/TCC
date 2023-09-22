def primo (numero_inteiro_positivo):
    if numero_inteiro_positivo > 1:
        for i in range(2,int(numero_inteiro_positivo/2)+1):
        	if (numero_inteiro_positivo % i) == 0:
            	return False		
        	else:
            	return True
    else:
        return False