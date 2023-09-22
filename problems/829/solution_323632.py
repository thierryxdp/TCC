def soma_h(n):
    '''retorna o valor da soma de "n" termos de "H"'''
    N=1
    d=1
    R=1
    for j in range(n):
        N=N+1
        d=d+1
        x=N/d
        R=R+x
    return round(R,2)