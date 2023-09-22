def lingua_p ( palavra ) :
    nova_palavra = ""
    for letra in palavra :
        nova_palavra += letra.lower ( )
        if ( letra in 'aãáAÃÁeéEÉiIoóôOÓÔuUúÚ' ) :
            nova_palavra += 'p'
            nova_palavra += letra.lower ( )
    return nova_palavra