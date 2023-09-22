def fatorial(num):
    ''' '''
    intervalo = list(range(1,num + 1))
    ordemFatorial = intervalo.reverse()
    indice = 0
    resultado = 1
    while indice < len(intervalo):
        resultado *= intervalo[indice]
        indice += 1
    return resultado