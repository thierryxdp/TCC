def total(lista_de_compras , produtos):
        valor = 0
    for item in lista_de_compras :
        if ( item in produtos.keys ( ) ) :
            valor += produtos [ item ]
    return valor