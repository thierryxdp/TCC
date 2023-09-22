def primo ( numero ) :
    divisores = qtd_divisores ( numero )
    if ( divisores == 2 ) :
        return True
    if ( divisores != 2 ) :
        return False