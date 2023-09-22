def soma_h(n):
    '''retorna o valor da soma de "n" termos de "H"'''
    x=0
    R=1
    for j in range(1,n+1):
        t=(1)**n/(x+1)
        R= R + t
    return round(R,2)