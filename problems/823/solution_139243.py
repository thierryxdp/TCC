def faltante(n):    
    contador = 0
    i = 1
    while i < len(n):
        if i not in n:
            return 
        contador += 1
    return contador