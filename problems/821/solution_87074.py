def fatorial(numero):
    '''funçao que calcula o fatorial de um numero'''
    fatorial = 1
    contador = 1
    while contador <= numero:
        fatorial = contador * fatorial 
        contador +=1
    return resultado