def eh_par(num):
    
    return num %2 ==0
    
def filtra_pares(t):
    pares=()
    if eh_par(t[0]):
        pares = pares + (t[0],)
    if eh_par(t[1]):
       pares=pares + (t[1],)                  
    if eh_par(t[2]):
       pares=pares +(t[2],)
    if eh_par(t[3]):                     
       pares = pares+ (t[3],)
    return pares