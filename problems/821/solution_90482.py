def fatorial(num):
    '''
    	Funcao que recebe um numero e retorna o seu fatorial
        int -> int
    '''
    i = 1
    fatorial = num
    while i < num:
        fatorial = fatorial * i
        i += 1
    return fatorial