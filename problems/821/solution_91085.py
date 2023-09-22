def fatorial(num):
    '''
    Funçao que recebe um numero e retorna 
    o fatorial dele
    int -> int
    '''
    i=1
    x=1
    while i <= num:
        x= x * i
        i=i+1
    return x