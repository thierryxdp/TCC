def fatorial(num):
    '''Função que retorna o cálculo do fatorial do número num.
    num=int->int'''
    t=list(range(1,num+1))
    z=1
    h=t[0]
    while z<len(t):
        h=h*t[z]
        z=z+1
    return h