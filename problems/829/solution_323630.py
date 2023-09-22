def soma_h(n):
    '''retorna o valor da soma de "n" termos de "H"'''
    R=1
    for j in range(1,n+1):
        t=(1)**n/(2*n+1)
        R= R + t
    return round(R,2)