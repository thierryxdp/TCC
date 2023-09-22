def colchao(ls, H, L):
    """
    Essa função tenta fazer uma cama passar pela porto, usando as dimensões do colchão e da porta
    lst, int, int -> Boolean
    """

    #A = ls[0]
    B = ls[1]
    C = ls[2]

    # Se B for maior que a largura, mas menor q a altura, tenta encaixar C na largura
    if (B >= L and B <= H) and C <= L:
        return True

    elif (B >= H and B <= L) and C <= H:
        return True

    else:
        return False

    #Caso teste ajudarJoaoComOColchao([200,80,50], 100, 50) -> True
    #Caso teste ajudarJoaoComOColchao([200,80,50], 70, 50) -> False
    #Caso teste ajudarJoaoComOColchao([200,80,50], 60, 110) -> True