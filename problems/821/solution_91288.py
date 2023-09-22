def fatorial(num):
    '''
       Dado um número(num) a função retorna o número fatorial
       do número dado como entrada.
       int -> int
    '''
    i=0
    fatorial=1
    numero=num
    while i<num:
        fatorial=fatorial*numero
        numero=numero-1
        i=i+1
    return fatorial