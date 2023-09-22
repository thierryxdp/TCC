def filtra_pares(tupla):
    a=tupla[0]%2
    b=tupla[1]%2
    c=tupla[2]%2
    d=tupla[3]%2
    
    if a == 0:
        return tupla[0]
    if b == 0:
        return tupla[0] + tupla[1]