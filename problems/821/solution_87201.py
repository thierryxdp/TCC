def fatorial(n):
    '''Função que tendo um numero n como entrada retorna o fatorial dele
int -> int'''
    i= 1
    mult= 1
    while i<n:
        mult= i*(i+1)
        i= i+1
    return mult