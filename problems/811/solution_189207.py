def colchao(medidas,H,L):
    """função que verifica se o colchão que joão comprar vai
    conseguir passar pela porta. medidas é uma lista com os 
    tamanhos inteiros A, B e C. H e L são os tamanhos inteiros
    da altura e largura da porta.
    lista, int, int -> bool"""
    M=medidas
    a=M[0]
    b=M[1]
    c=M[2]
    if b > H:
        if a > L:
            if c > L:
                return False
            else: 
                return True
        if c > L:
            if a > L:
                return False
            else:
                return True
    if c > H:
        if b > L:
            if a >:
                return False
            else: 
                return True
        if a > L:
            if b > L:
                return False
            else:
                return True
    if a > H:
        if b > L:
            if c >:
                return False
            else: 
                return True
        if c > L:
            if b > L:
                return False
            else:
                return True