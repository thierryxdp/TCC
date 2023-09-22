def filtra_pares(a, b, c, d):
    
   "filtra os pares"
   
    y = (a, b, c, d)
    
    x = y[0: :2]
    
    if x != y[::2]:
        return none