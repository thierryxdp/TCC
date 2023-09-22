def colchão(medidas,x,y):
    """Função que recebe como entrada uma lista com as dimensões A, B e C
    do colchão em centímetros, ordenadas da menor para a maior, e dois
    inteiros H e L, correspondentes respectivamente a altura e a largura
    das portas em centímetros. A função retorna True se o colchão passa pela
    porta e False caso o contrário.
    lista(int,int,int)-> int,int
    """
    
    if medidas[2]<= x and medidas[2]<= y:
        return True
    elif medidas[2]<=x and medidas[2]>y:
        if medidas[1]<=y:
            return True
    elif medidas[2]<=x and medidas[2]>y:
        if medidas[0]<=y:
            return True
    elif medidas[2]>x and medidas[2]<=y:
        if medidas[0]<=x:
            return True
    elif medidas[2]>x and medidas[2]<=y:
        if medidas[1]<=x:
            return True
    elif medidas[1]<=x and medidas[1]<=y:
        return True
    elif medidas[1]<=x and medidas[1]>y:
        if medidas[0]<=y:
            return True
    elif medidas[1]>x and medidas[1]<=y:
        if medidas[0]<=x:
            return True
    else:
        return False