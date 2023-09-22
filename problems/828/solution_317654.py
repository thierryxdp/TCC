from math import sqrt
def primo (numero_inteiro_positivo):
    if numero_inteiro_positivo > 1:
        for i in range(2,int(sqrt(numero_inteiro_positivo))+1):
        	if (numero_inteiro_positivo % i) == 0:
            	return False		
            if (numero_inteiro_positivo % 11) == 0:
                return False
            if (numero_inteiro_positivo % 17) == 0:
                return False
            if (numero_inteiro_positivo % 3) == 0:
                return False
            if (numero_inteiro_positivo % 13) == 0:
                return False
            if (numero_inteiro_positivo) == 11:
                return False
        	else:
            	return True
    else:
        return False