def primo (n):
    '''Funcao que, dado um numero inteiro positivo, retorna se este numero é primo ou não.
    int->bool'''
    primo = True
    i = 2
    while i <= n/2 and primo:
        if n % i == 0:    # se num eh multiplo de i
            primo = False   # num nao pode ser primo
        i += 1
    return primo