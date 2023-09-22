filtra_pares(tupla):
    if not (tupla):
        return 0
    
    par = (tupla[0:3]%2 == 0)
    
    if par:
        return tupla[0:]
    else:
        return 0