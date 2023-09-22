def fatorial(num):
    '''
        Função que calculo o fatorial de um número num
        int -> int
    '''
    int(num)
    if num < 0:
        return -1
    i=1
    contador=1
    while i <= num:
        contador= contador*i
        i=i+1
    return contador