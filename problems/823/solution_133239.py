def faltante(x):
    '''Função que dada uma lista descubra qual o número
    inteiro do intervalo falta. list-->int.'''
    y=[0]+x+[0]
    t=0
    h=list(range(len(x)+1))+[x]+[0]
    while t<=len(y):
        if h[t]!=y[t]:
            return y[t-1]+1
        t+=1