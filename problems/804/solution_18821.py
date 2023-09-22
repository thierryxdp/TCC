def filtra_pares(algarismos):
    """Função que recebe uma tupla com quatro elementos inteiros e retorna uma nova
apenas com os algarismos pares na mesma ordem em que já se encontravam.
    tuple -> tuple"""
    
    pares = ()
    
    if algarismos[0]%2 == 0:
        pares = pares + (algarismos[0],)
    if algarismos[1]%2 == 0:
        pares = pares + (algarismos[1],)
    if algarismos[2]%2 == 0:
        pares = pares + (algarismos[2],)
    if algarismos[3]%2 == 0:
        pares = pares + (algarismos[3],)
        
    return pares