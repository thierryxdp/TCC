def fatorial(n):
    '''funcao que recebe um numero inteiro positivo n como entrada e calcula e retorna o fatorial deste numero n
    int -> int'''
    i=1
    n_fatorial=n
    while i<n:
        n_fatorial=n_fatorial*i
        i=i+1
    return n_fatorial