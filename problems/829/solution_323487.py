def soma_h(n):
    '''Calcula e retorna o valor H com N termos.
    int,int -> int'''
    total = []
    for i in range(1,n):
        total = [(1/i) + n]
    return total