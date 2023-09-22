def carros(n,c):
    '''calcula o número de carros - convencionais ou não - necessários para que n
    amigos realizem uma viagem de carro com capacidade c; int,int -> int'''
    i = (n//c)+ 1
    return i