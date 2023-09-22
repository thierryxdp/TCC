def filtra_pares(tupla):
    '''dado uam tupla com quatro elementos inteiros, 
    retorna uma nova tupla contendo apenas elementos
    pares da tupla original.
    tuple --> tuple'''
    
    L=()
    a,b,c,d = tupla
    
    if a%2==0 :
        L= L + (a,)
        
    if b%2==0:
        L =L + (b,)
        
    if c%2==0:
        L = L + (c,)
        
    if d%2==0:
        L = L + (d,)
        
        return L