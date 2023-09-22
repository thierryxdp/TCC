def filtra_pares(tupla):
       
    par = (tupla[0]%2 == 0)
    
    if par:
        
        return 1 + filtra_pares(tupla[1:])
    else:
        return filtra_pares(tupla[1:])