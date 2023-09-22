def soma_h(n):
    '''Função que calcula e retorna o valor da soma com 'n'
    termos.
    int->float'''
    
    soma=0
    
    for i in range(1,n):
        
        soma+=i
    return round(soma,2)