def filtra_pares(a, b ,c, d):
    """Dados quatro elementos retorna apenas os pares.
       int int int int -> int pares"""
    
    todos = [a, b, c, d]
    pares = []
    
    for numero in todos:
        if numero % 2 == 0:
            pares.append(numero)
            
     return pares[]