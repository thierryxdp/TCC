def conta_numero ( m , numero ) :
    linhas = len(m)
    if ( linhas == 0 ) :
        return 0
    quantidade = 0
    for linha in m :
        for elemento in linha :
            if ( numero == elemento ) :
                quantidade += 1
    return quantidade