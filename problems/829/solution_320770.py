def soma_h(n):
    '''
    Função que recebe o argumento n e retorna 1+1/2+1/3+...+1/n
    '''
    sum = 0
    for i in range(n):
    	sum = sum+1/(i+1)
    return round(sum,2)