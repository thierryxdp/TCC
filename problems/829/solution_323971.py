def soma_h(n):
    ''' Função que soma n termos retornando com 2 casas 
    	decimais.
        int--->float'''
    r=()
    x=n+1
    for i in range(1,x):
        r=r+(1/i,)
        
    return round(sum(r),2)