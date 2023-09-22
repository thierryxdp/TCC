def qtd_divisores(x):
    contador = 0
    for n in range(1, x+1):  
        if(x % n  == 0):
            contador = contador + 1
    
	return contador