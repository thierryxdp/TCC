def fatorial(num):
    '''função que recebe um número e retorna o fatorial desse número.
    int -> int'''
    
    fatorial = 1
    contagem = 1
    while contagem <= num:
        fatorial = fatorial * contagem
        contagem = contagem + 1
    return fatorial