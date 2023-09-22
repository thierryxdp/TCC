def colchao(ls, H, L):
    """
    Essa função tenta fazer uma cama passar pela porto, usando as dimensões do colchão e da porta
    lst, int, int -> Boolean
    """

    A = ls[0]
    B = ls[1]
    #C = ls[2]

    # Se A for maior que a largura, mas menor q a altura, tenta encaixar B na largura
    if (A >= L and A <= H) and B <= L:
        return True

    elif (A >= H and A <= L) and B <= H:
        return True

    else:
        return False

    #Caso teste ajudarJoaoComOColchao([50,80,200], 100, 50) -> True
    #Caso teste ajudarJoaoComOColchao([50,80,200], 70, 50) -> False
    #Caso teste ajudarJoaoComOColchao([50,80,200], 60, 110) -> True