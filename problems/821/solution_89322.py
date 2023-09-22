def fatorial(n):
    '''
       Função que recebe um numero e calcula o fatorial desse
       numero
       int -> int
    '''
    i=1
    contador=1
    while i <= n:
        contador= contador*i
        i=i+1
    return contador