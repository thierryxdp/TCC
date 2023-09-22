def colchao(medidas: list, H: float, L: float) -> bool:
    """Diz se é possível ou não passar com um colchão de medidas dadas, em cm,
       pela porta de medidas H x L, em cm
       
       Parameters:
       medidas: lista com as três dimensões do colchão em centímetros, da menor para a maior
       H: altura da porta em centímetros
       L: largura da porta em centímetros
       
       Returns:
       Se for possível passar: True; caso não, False
    """
    
    if medidas[0] <= H:
        if medidas[1] <= L:
            return 'True'
    if medidas[0] <= L:
        if medidas[1] <= H:
            return 'True'
        else:
            return 'False'
    else:
        return 'False'