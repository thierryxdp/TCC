def fatorial(n):
    '''Calcula o fatorial de umnúmero. int -> inte'''
    resultado = 1
    cont = 0
    while cont < n:
        resultado = resultado * cont
        cont = cont + 1	
    return resultado