def soma_h(n):
    '''Função que retorna o valor de H com N termos, dado o número de termos n;int->float'''
    soma=0
    fim=n+1
    for i in range(1,fim):
        h=(1/i)
        soma=soma+h
    return round(soma,2)