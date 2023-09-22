def filtra_pares(n):
    
    acumula =()
    if n[0] % 2 == 0:
        acumula += (n[0],)
    else:
        acumula = acumula
        
    if n[1] % 2 == 0:
         acumula += (n[1],)
    else:
        acumula = acumula
        
    if n[2] % 2 == 0:
          acumula += (n[2],)
    else:
        acumula = acumula
        
    if n[3] % 2 == 0:
          acumula += (n[3],)
    else:
        acumula = acumula
    return acumula