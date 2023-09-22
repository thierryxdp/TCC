def fatorial(n):
    ''' '''
    bloco=list(range(n))
    contador=0
    acumulador=()
    while contador<len(bloco):
        anterior=contador-1
        fatorial=bloco[anterior]*bloco[contador]
        acumulador=acumulador+fatorial
        contador=contador+1
    return acumulador[anterior]*acumulador[contador]