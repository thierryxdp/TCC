def fatorial(numero):
    '''Dado um número, a função deve calcular e retornar o
    fatorial deste número;
    int->int'''
    n2=numero-1
    fatorial_numero= numero
    
    while(n2>0):
        fatorial_numero= fatorial_numero*n2
        n2= n2-1
        
    return (fatorial_numero)