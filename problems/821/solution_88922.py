def fatorial(x):
    '''
    funcao retorna o fatorial do número x sem usar o fatorial do math
    '''
    num=list(range(x+1))
    list.remove(num,0)
    i=0
    fatorial=1
    while i<len(num):
        fatorial=fatorial*num[i]
        i=i+1
    return fatorial