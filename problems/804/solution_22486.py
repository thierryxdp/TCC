def filtra_pares(x,y,z,w):
    
    d =()
    
    if x%2 == 0 or y%2 == 0 or z% == 0 or w% == 0:
        d = d + (x,y,z,w,)
    if x%2 == 0 and y%2 == 0 and z% == 0 and:
        d = d + (x,y,z,)
    if x%2 == 0 and y%2 == 0:
        d = d + (x,y,)
    if x%2 == 0:
        d = d + (x,)
    return d