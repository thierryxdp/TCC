def soma_h(n):
    '''função que retorna o número somando todas as frações dado n como entrada; int => float'''
    soma=0
    for c in range(1,n+1):
        inverso=(1/c)
        soma+=inverso
    return round(soma,2)