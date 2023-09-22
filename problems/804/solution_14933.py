def filtra_pares(s):
    """função que retorna somente os números 
    pares da tupla original
    tuple=>tuple
    resultado_filter = filter(lambda filtragem: 
                              filtragem % 2 == 0, s)
    tuple_final = tuple(resultado_filter)  # transforma em tuple
    return tuple_final  # retornando tuple#Start your python function here"""
    tupla_final=()
    if s[0]%2==0:
        tupla_final+=s[0]
    elif s[1]%2 == 0:
		tupla_final+=s[1]
    elif s[2] % 2 == 0:
        tupla_final+=s[2]
    elif s[3] % 2 ==0:
        tupla_final+=s[3]
    
    return tupla_final