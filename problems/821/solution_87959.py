def fatorial(n):
    """Funcao que dado um numero n, calcula e retorna o 
    fatorial deste numero;
    int->int"""
    
    L=list(range(1,n+1))
    i=0
    F=1
    
    while i<len(L):
        F=F*L[i]
        i=i+1
    return F