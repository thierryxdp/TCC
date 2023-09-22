def soma_h(n):
    ''' calcula e retorna o valor de H com N termos.
    int -> float'''
    a=0
    for i in range (1,n+1):
        a = a + 1/i
        x = round(a,2)
    return x