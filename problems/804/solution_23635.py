def filtra_pares (tupla):
    ''' função que retorna uma nova tupla contendo apenas elementos pares
    da tupla original'''
    x=()
    if tupla[0]%2==0:
        x= x + (tupla [0],)
   
    if tupla[1]%2==0:
        x=x+  (tupla [1],)
    if tupla[2]%2==0:
        x=x+  (tupla [2],)
        
    if tupla[3]%2==0:
        x=x+ (tupla [3],)
    return x