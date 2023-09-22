def fatorial(num):
    '''Faça uma função que dado um número, calcule o fatorial deste número.'''
    #int > int
    lista = [num]
    n = 1
    while n != num and n <= num:
        lista = lista + [n]
        n = n+1
    fatorial = 1
    for x in lista:
         fatorial = fatorial * x 
    return fatorial