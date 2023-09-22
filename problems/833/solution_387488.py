def conta_numero(numero,matriz):
    '''Conta a quantas vezes o numero se repete dentro da matriz;
    int,list(list(int))->int'''
    
    repeticoes=0
    
    if numero in matriz:
        repeticoes+=1
        return repeticoes