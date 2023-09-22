def fatorial(n):
    ''' '''
    bloco=list(range(n))
    contador=0
    while contador<len(bloco):
        anterior=contador-1
        fatorial=bloco[anterior]*bloco[contador]
        contador=contador+1
    return fatorial