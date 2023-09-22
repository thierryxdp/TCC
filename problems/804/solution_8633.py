def filtra_pares(n):
    """Essa função, dada uma tupla com quatro elementos inteiros como parâmetro,
    retorna uma nova tupla contendo apenas os elementos pares da tupla original
    tuple -> tuple"""
    acumula =()
    if n[0] % 2 == 0:
        acumula += (n[0],)
    else:
        acumula = acumula
        
    if n[1] % 2 == 0:
         acumula += (n[1],)
    else:
        acumula = acumula
        
    if n[2] % 2 == 0:
          acumula += (n[2],)
    else:
        acumula = acumula
        
    if n[3] % 2 == 0:
          acumula += (n[3],)
    else:
        acumula = acumula
    return acumula