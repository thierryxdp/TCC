def filtra_pares(x):
    "retorna algu lengoço aí"
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    tf=()
    if a%2!=1:
     tf= tf+(a,)
    if b%2!=1:
     tf= tf+(b,)
    if c%2!=1:
     tf= tf+(c,)
    if d%2!=1:
     tf= tf+(d,)
   return tf