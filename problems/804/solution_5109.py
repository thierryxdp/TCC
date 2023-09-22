def filtra_pares(n):
    "Essa função retorna os numeros pares de uma função"
    x =()
    if n[0] % 2 == 0:
        x = x + (n[0],)
    else:
        x = x
        
    if n[1] % 2 == 0:
        x = x + (n[1],)
    else:
        x = x
        
    if n[2] % 2 == 0:
        x = x + (n[2],)
    else:
        x = x 
        
    if n[3] % 2 == 0:
        x = x + (n[3],)
    else:
        x = x
    return x