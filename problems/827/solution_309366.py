def qtd_divisores (numero):
    '''função que retorna quantos divisores o número tem
    int -> int'''
    
    contador = 0
    
    for numerof in range(numero+1):
        if numerof !=0:
        	if numero/numerof == int(numero/numerof):
            	contador += 1
    return contador