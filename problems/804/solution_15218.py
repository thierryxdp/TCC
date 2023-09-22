def filtra_pares(x):
    "Retorne os pares de uma dada tupla; tupla->tupla"
    a = x[0] 
    b = x[1] 
    c = x[2]
    d = x[3]
    tf = ()
    if a%2!=1:
        tf=tf + (w,)
    if b%2 != 1:
		tf= tf + (x,)
    if c % 2 != 1:
        tf= tf + (y,)
    if d % 2 !=1:
        tf= tf + (z,)
    
    return tupla_final