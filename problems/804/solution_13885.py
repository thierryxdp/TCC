def filtra_pares(num):
    """funcao que recebe uma tupla com quatro elementos inteiros e retorna
    outra tupla contendo os numeros pares na mesma ordem em que se encontravam
    tuple -> tuple"""
    
    t = ( )
    
    if num[0]%2 == 0:
        t = t+(num[0],)
    
    else:
        t = t
    
    if num[1]%2 == 0:
        t = t+(num[1],)
    
    else:
        t = t
    
    if num[2]%2 == 0:
        t = t+(num[2],)
    
    else:
        t = t
    
    if num[3]%2 == 0:
        t = t+(num[3],)
    
    else:
        t = t
    
    return t