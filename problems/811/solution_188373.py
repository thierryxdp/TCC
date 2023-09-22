def colchao(ls, L, H):
    """
    Essa função tenta fazer uma cama passar pela porto, usando as dimensões do colchão e da porta
    lst, int, int -> Boolean
    """

    A = ls[0]
    B = ls[1]
    #C = ls[2]

     # Se A for menor que a largura, tenta encaixar B na altura
    if A <= L and B <= H:
        return True

    elif A <= H and B <= L:
        return True
    
    else:
        return False

    #Caso teste colchao([50,80,200], 100, 50) -> True
    #Caso teste colchao([50,80,200], 70, 50) -> False
    #Caso teste colchao([50,80,200], 60, 110) -> True