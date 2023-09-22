def soma_h(n): 
    '''função que calcule e retorne o valor de 'H' com 'n'termos.
    O valor de 'H' é definido como H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
    int -> float'''
    
    H = 0
    for x in range(1,n+1):
        numero = 1/x
        H += numero
    return round(H,2)