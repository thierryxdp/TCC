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
        tupla_final=tupla_final + int(s[0])
    if s[1]%2 == 0:
		tupla_final= tupla_final + int(s[1])
    if s[2] % 2 == 0:
        tupla_final= tupla_final + int(s[2])
    if s[3] % 2 ==0:
        tupla_final= tupla_final + int(s[3])
    
    return tupla_final