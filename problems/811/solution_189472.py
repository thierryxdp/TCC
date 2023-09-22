def  colchao ( m , h , l ):
    """funcao que retorna True se o colchao passar pela porta, e False, caso
    contrario"""
    m . sort ()
    se  m [ 0 ] >  h :
        se  m [ 0 ] >  l :
            retornar  falso
        elif  m [ 1 ] >  l :
            retornar  falso
        mais :
            retornar  verdadeiro
    elif  m [ 1 ] >  h :
        retornar  falso
    mais :
        retornar  verdadeiro