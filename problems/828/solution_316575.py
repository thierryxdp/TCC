def qtd_divisores ( numero ) :
    divisores = 0
    c1 = 0
    while ( c1 < numero ) :
        divisor = c1 + 1
        if ( numero % divisor == 0 ) :
            divisores += 1
        c1 += 1
    return divisores

def primo ( numero ) :
    divisores = qtd_divisores ( numero )
    if ( divisores == 2 ) :
        return True
    if ( divisores != 2 ) :
        return False