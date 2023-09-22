def primo (numero):
    '''função que dado um número inteiro, retorna se é ou não
    número primo
    int ->bool'''
    
    contador = 0
    
    for numerof in range(numero+1):
        if numerof !=0:
        	if numero/numerof == int(numero/numerof):
            	contador += 1
    return contador <= 2