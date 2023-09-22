def filtra_pares(tupla):
    '''dado uam tupla com quatro elementos inteiros, 
    retorna uma nova tupla contendo apenas elementos
    pares da tupla original.
    tuple --> tuple'''
    
    L=()
    
    
    if tupla[0]%2==0 :
        L= L + tupla[0]
        
    if tupla[1]%2==0:
        L =L + tupla[1]
        
    if tupla[2]%2==0:
        L = L + tupla[2]
        
    if tupla[3]%2==0:
        L = L + tupla[3]
        
        return L