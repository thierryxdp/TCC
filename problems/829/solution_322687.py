def soma_h(N):
    '''Uma função que retorna a soma dos inversos em seguencia
    até o numero N int->float(Até duas casas)'''
    h=0
    for i in range(1,N+1):
        h=h+(1/i)
    h = round(h,2)
    return h