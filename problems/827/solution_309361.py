def qtd_divisores(n):
    '''
    Funçao que conta a quantidade de divisores de um numero
    int->int
    '''
    qtd=[1,n]
    if n==0:
        list.clear(qtd)
	elif n<0:
        list.clear(qtd)
	else:    
        for i in range(2,n-1):        
       		if n%i == 0:                        
            	list.append(qtd,i)
		
    return len(qtd)