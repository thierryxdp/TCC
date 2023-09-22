def soma_h(n):
    '''retorna o valor da soma de "n" termos de "H"'''
    N=1
    d=1
    R=0
    for j in range(n):
        d=d+1
        x=N/d
        R=R+x
    return round(R,2)