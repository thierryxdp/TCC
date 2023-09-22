def colchao(medidas,H,L):
    """Função que recebe como entrada uma lista com as dimensões A, B e C
    do colchão em centímetros, ordenadas da menor para a maior, e dois
    inteiros H e L, correspondentes respectivamente a altura e a largura
    das portas em centímetros. A função retorna True se o colchão passa pela
    porta e False caso o contrário.
    lista(int,int,int)-> int,int
    """
    
    if medidas[2]<= H and medidas[2]<= L:
        return True
    elif medidas[2]<=H and medidas[2]>L:
        if medidas[1]<=L:
            return True
    elif medidas[2]<=H and medidas[2]>L:
        if medidas[0]<=L:
            return True
    elif medidas[2]>H and medidas[2]<=L:
        if medidas[0]<=H:
            return True
    elif medidas[2]>H and medidas[2]<=L:
        if medidas[1]<=H:
            return True
    elif medidas[1]<=H and medidas[1]<=L:
        return True
    elif medidas[1]<=H and medidas[1]>L:
        if medidas[0]<=L:
            return True
    elif medidas[1]>H and medidas[1]<=L:
        if medidas[0]<=H:
            return True
    else:
        return False