def fatorial(numero):
    '''funcao que retorna o calculo do fatorial de um numero
    int->int'''
    fatorial=1
    i=1
    while i<=numero:
        fatorial*=i
        i+=1
    return fatorial