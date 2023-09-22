def fatorial(n):
    '''Função que tendo um numero n como entrada retorna o fatorial dele
int -> int'''
    i= n
    mult= 0
    while i>1:
        mult= i*(i-1)
        i= i-2
    return mult