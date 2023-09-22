def colchao(medidas,H,L):
    '''Dado as medidas do colchao e da porta, retornará 'True' se
    o colchão passar por ela, e 'False' caso não passe.(lista,int,int=>bool)'''

    if medidas[0]<= max(H,L) and medidas[1] <= max(H,L):
        return True

    if medidas[0]<= max(H,L) and medidas[2] <= max(H,L):
        return True
    
    if medidas[1]<= max(H,L) and medidas[2] <= max(H,L):
        return True

    else:
        return False