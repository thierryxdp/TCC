def conta_numero(numero,matriz):
    '''Conta a quantas vezes o numero se repete dentro da matriz;
    int,list(list(int))->int'''
    
    rep=0
    
    if numero in matriz:
        rep+=1
        return rep