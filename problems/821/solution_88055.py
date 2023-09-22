def fatorial(n):
    """função que dado um número calcula o fatorial deste número
    int -> <fatorado>"""
    i     = 1  
    fatorado = 1  
    
    while i <= n:
        fatorado = fatorado * i 
        i = i + 1
	return fatorado