def soma_h(N):
    soma=0
    for i in range(1,N+1):
        f=(1/i)
        soma+=f
    return round(soma,2)
'''dado um numero inteiro calcula a soma dos seus 
inversos.
int->float'''