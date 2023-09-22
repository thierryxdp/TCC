def filtra_pares(tupla):
    '''dado uam tupla com quatro elementos inteiros, 
    retorna uma nova tupla contendo apenas elementos
    pares da tupla original.
    tuple --> tuple'''
    
    F=()
    
    tupla = a,b,c,d
    
    if a%2==0 :
        F=F+(a,)
        
    if b%2==0:
        F=F+(b,)
        
    if c%2==0:
        F=F+(c,)
        
    if d%2==0:
        F=F+(d,)
        
        return F