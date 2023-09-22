def filtra_pares(x):
    "Retorne os numeros pares de uma dada tupla; tupla-> tupla"
    a = x[0] 
    b = x[1] 
    c = x[2]
    d = x[3]
    s = ()
    if a%2!=1:
        s=s + (a,)
    if b%2!=1:
		s=s + (b,)
    if c%2!=1:
        s=s + (c,)
    if d%2!=1:
        s=s + (d,)
    
    return s