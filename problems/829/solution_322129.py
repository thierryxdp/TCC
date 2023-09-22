def soma_h(soma):
    '''Funcao recebe um numero N e retorna a soma 1/1 + 1/2... 1/N por exemplo
inst -> float'''
    contador = 0
    acumulador = []
    h = 0
    while (len(acumulador) < soma):
        acumulador += [contador+1]
        contador +=1 
    for i in acumulador:
        h += 1/i
    return roun(h,2)