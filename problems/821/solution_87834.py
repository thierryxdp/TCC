def fatorial(num):
    '''função que recebe um numero num e retorna o fatorial deste numero;
    int-->int'''
    numero=list(range(1,num+1))
    proximo=0
    fatorial=1
    while proximo<len(numero):
        fatorial=fatorial*numero[proximo]
        proximo=proximo+1
    return fatorial