def faltante(intervalo):
    '''retorna o número que falta, dado untervalo de peças no quebra-cabeça;
    list->int'''
    total=list(range(min(intervalo),(max(intervalo)+1)))
    i=1
    d=0
    while i<len(total):
        if i == total[d]:
            d=d+1
        i=i+1
    return d