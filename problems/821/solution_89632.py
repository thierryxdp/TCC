def fatorial(numero):
    '''funcao que calcula o fatorial de um numero dado.
    int -> int'''
    fatorial = 0
    contador = 1
    while contador < numero:
        fatorial =  fatorial * numero*(numero - contador)
    	contador = contador + 1
    return fatorial