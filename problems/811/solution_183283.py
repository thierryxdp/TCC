def colchao(medidas,h,l):
    '''Função que recebe as dimensoes de um colchao e as da porta,
    verificando se o colchao passa pela porta (true) ou se não
    passa (false)
    float,float,flaot->bool'''
    if l >= medidas [0] and h>= medidas [1]:
        return true
    else:
        return false