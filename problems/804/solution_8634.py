def filtra_pares(n):
    """Essa função, dada uma tupla com quatro elementos inteiros como parâmetro,
    retorna uma nova tupla contendo apenas os elementos pares da tupla original
    tuple -> tuple"""
    tupla_final =()
    if n[0] % 2 == 0:
        tupla_final += (n[0],)
    else:
        tupla_final = tupla_final
        
    if n[1] % 2 == 0:
         tupla_final += (n[1],)
    else:
        tupla_final = tupla_final
        
    if n[2] % 2 == 0:
          tupla_final += (n[2],)
    else:
        tupla_final = tupla_final
        
    if n[3] % 2 == 0:
          tupla_final += (n[3],)
    else:
        tupla_final = tupla_final
    return tupla_final