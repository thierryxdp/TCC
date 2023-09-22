def fatorial(num):
    '''funcao que calcula o fatorial de um numero dado.
    int -> int'''
    fatorial = 0
    while num > 0:
        fatorial =  fatorial * num
    	num = num - 1
    return fatorial