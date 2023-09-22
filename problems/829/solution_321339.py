def soma_h(n):
    '''Função que calcula e retorna o valor da soma com 'n'
    termos.
    int->float'''
    
    soma=0
    
    for i in range(1,n):
        i=1/i
        soma+=i
        soma=soma+1/n
    return round(soma,2)