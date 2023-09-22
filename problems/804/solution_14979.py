def filtra_pares(s):
    """função que retorna somente os números 
    pares da tupla original
    tuple=>tuple
    resultado_filter = filter(lambda filtragem: 
                              filtragem % 2 == 0, s)
    tuple_final = tuple(resultado_filter)  # transforma em tuple
    return tuple_final  # retornando tuple#Start your python function here"""
    w = s[0] 
    x = s[1] 
    y = s[2]
    z = s[3]
    if w%2==0:
        tupla_final=tupla_final + (w,)
    if x%2 == 0:
		tupla_final= tupla_final + (x,)
    if y % 2 == 0:
        tupla_final= tupla_final + (y,)
    if z % 2 ==0:
        tupla_final= tupla_final + (z,)
    
    return tupla_final