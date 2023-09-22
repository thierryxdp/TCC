def qtd_divisores(n):
    '''
    Funçao que conta a quantidade de divisores de um numero
    int->int
    '''
    qtd=[1,n]
    for i in range(2,n-1):
        if n%i == 0:                        
            list.append(qtd,i)
		elif n==0:   		
            list.clear(qtd)
    return len(qtd),qtd