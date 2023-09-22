def soma_h(n):
    '''Retorna a soma da séria harmônica até o termo n.
    int --> float'''
    
	soma = 0

    for i in range(1,n+1):
        soma = soma + (1/i)
        
    return round(soma,2)