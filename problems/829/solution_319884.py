def soma_h(N):
    '''função que calcula a soma de 'h' sendo h=1+1/2+1/3+1/4...1/N.
       int->float '''
    soma=0
    for numero in list(range(1,N+1)):
        soma=soma+1/(numero)
    return soma