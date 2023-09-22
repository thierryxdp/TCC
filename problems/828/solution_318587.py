def primo (numero_int_pos):
    """função que dado um número inteiro positivo verifica se esse número é primo.
    int -> bool"""
     for x in range(2,numero_int_pos):
        if numero_int_pos % x ==0:
            return False
    else:
            return True