def qtd_divisores (num):
    '''retorna a quantidade de divisores que o
    argumento possui
    complex -> complex'''
    
    j = 0
    
    for i in range(1,num+1):
        if num%i == 0:
            j += 1
            
	return j