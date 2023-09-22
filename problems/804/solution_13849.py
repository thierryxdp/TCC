def filtra_pares(s):
    """função que retorna somente os números 
    pares da tupla original
    tuple=>tuple"""
    resultado_filter = filter(lambda filtragem: 
                              filtragem % 2 == 0, s)
    tuple_final = tuple(resultado_filter)  # transforma em tuple
    return tuple_final  # retornando tuple