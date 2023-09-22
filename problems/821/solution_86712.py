from functools import reduce
def fatorial(num):
    ''' '''
    intervalo = list(range(1,num + 1))
    ordemFatorial = intervalo.reverse()
    return reduce(lambda x,y:x*y,intervalo)