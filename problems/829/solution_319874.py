def soma_h(N):
    '''função que calcula a soma de 'h' sendo h=1+1/2+1/3+1/4...1/N.
       int->float '''
    contador=0
    for numero in range(1,N+1):
        h=1/numero
        soma=contador+h
    return soma+1