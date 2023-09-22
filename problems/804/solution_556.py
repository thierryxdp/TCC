def filtra_pares(elementos):
    """funcao que retorna os elementos pares de uma tupla com quatro elementos;
    tuple -> tuple"""
    
    n1 = elementos[0]
    n2 = elementos [1]
    n3 = elementos[2]
    n4 = elementos[3]
    
    elementos_pares = ()
    
    if n1 % 2 == 0:
        elementos_pares = elementos_pares + (n1, )
    
    if n2 % 2 == 0:
        elementos_pares = elementos_pares + (n2, )
        
    if n3 % 2 == 0:
        elementos_pares = elementos_pares + (n3, )
        
    if n4 % 2 == 0:
        elementos_pares = elementos_pares + (n4, )
        
    return elementos_pares