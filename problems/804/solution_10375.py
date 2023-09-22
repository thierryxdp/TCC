def filtra_pares(tupla):
    """Função que filtra os termos pares de uma tupla de 4 termos, que retorna
    os termos pares.
    int -> int"""
    tuplaFinal = ()
    tupla_a = tuplaFinal + (tupla[0],)
    tupla_b = tuplaFinal + (tupla[1],)
    tupla_c = tuplaFinal + (tupla[2],)
    tupla_d = tuplaFinal + (tupla[3],)
    a = tupla[0]%2
    b = tupla[1]%2
    c = tupla[2]%2
    d = tupla[3]%2
    if a == 0 and b == 0 and c == 0 and d == 0:
        return tupla
    elif a == 0 and b == 0 and c == 0:
        return tupla_a + tupla_b + tupla_c
    elif a == 0 and b == 0 and d == 0:
        return tupla_a + tupla_b + tupla_c
    elif a == 0 and c == 0 and d == 0:
        return tupla_a + tupla_c + tupla_d
    elif b == 0 and c == 0 and d == 0:
        return tupla_b + tupla_c + tupla_d
    elif a == 0 and b == 0:
        return tupla_b + tupla_b
    elif a == 0 and c == 0:
        return tupla_a + tupla_c
    elif a == 0 and d == 0:
        return tupla_a + tupla_d
    elif b == 0 and c == 0:
        return tupla_b + tupla_c
    elif b == 0 and d == 0:
        return tupla_b + tupla_d
    elif c == 0 and d == 0:
        return tupla_c + tupla_d
    elif a == 0:
        return tupla_a
    elif b == 0:
        return tupla_b
    elif c == 0:
        return tupla_c
    elif d == 0:
        return tupla_d
    else:
        return tuplaFinal