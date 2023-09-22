def filtra_pares(tupla):
    """Função que filtra os termos pares de uma tupla de 4 termos, que retorna
    os termos pares.
    int -> int"""
    tuplaFinal = ()
    tupla_a = tuplaFinal + (tupla[0],)
    tupla_d = tuplaFinal + (tupla[3],)
    a = tupla[0]%2
    b = tupla[1]%2
    c = tupla[2]%2
    d = tupla[3]%2
    if a == 0 and b == 0 and c == 0 and d:
        return tupla
    elif a == 0 and b == 0 and c == 0:
        return tupla[0:2]
    elif a == 0 and b == 0 and d == 0:
        return tupla[0:3] + tupla_d
    elif a == 0 and c == 0 and d == 0:
        return tupla_a + tupla[2:4]
    elif b == 0 and c == 0 and d == 0:
        return tupla[1:4]
    elif a == 0 and b == 0:
        return tupla[0:1]
    elif a == 0 and c == 0:
        return tupla[0:3:2]
    elif a == 0 and d == 0:
        return tupla[0:4:3]
    elif b == 0 and c == 0:
        return tupla[1:2]
    elif b == 0 and d == 0:
        return tupla[1:4:2]
    elif c == 0 and d == 0:
        return tupla[2:4]
    elif a == 0:
        return (tupla[0])
    elif b == 0:
        return (tupla[1])
    elif c == 0:
        return (tupla[2])
    elif d == 0:
        return (tupla[3])
    else:
        return