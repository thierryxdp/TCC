def eh_quadrada ( matriz ) :
    linhas = len ( matriz )
    if ( linhas == 0 ) :
        return True
    quadrada = "sim"
    c1 = 0
    while ( c1 < len ( matriz ) ) :
        colunas = len ( matriz [ c1 ] )
        if ( linhas != colunas ) :
            quadrada = "nao"
        c1 += 1
    if ( quadrada == "sim" ) :
        return True
    if ( quadrada == "nao" ) :
        return False