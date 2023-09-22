def filtra_pares(x)
   tupla_vazia= ()
    
    if x[0]%2==0:
        tupla_vazia = tupla_vazia + (x[0],)
    if x[1]%2==0:
        tupla_vazia = tupla_vazia + (x[1],)
        
        return tupla_vazia