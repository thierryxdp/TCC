def conta_numero ( matriz , numero ) :
    linha = len(matriz)
    if ( linhas == 0 ) :
        return 0
    quantidade = 0
    for linha in matriz :
        for elemento in linha :
            if ( numero == elemento ) :
                quantidade += 1
    return quantidade