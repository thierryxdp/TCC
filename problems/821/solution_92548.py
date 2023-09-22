def fatorial(n):
    """ Função que recebe um número como entrada e retorna o calculo fatorial
    	desse número. int --> int """
    i = 0
    fatorial = 1
    while i < n:
        fatorial *= n - i
        i += 1
    return fatorial