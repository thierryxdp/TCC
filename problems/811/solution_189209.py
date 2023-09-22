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
    if a and b > L:
        return False
    if a and c > L:
        return False
    if c and b > L:
        return False