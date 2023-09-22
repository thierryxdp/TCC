def colchao(medidas,H,L):
    """Função que dadas a lista com as dimensões do colchão
    em centímetros, ordenadas da menor para a maior, e dois
    inteiros H e L, correspondentes respectivamente a altura
    e a largura das portas em centímetros, retorna True se o
    colchão passa pelas portas e False caso contrário;
    list, int, int -> bool"""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if A<=H and B<=L or A<=H and C<=L:
        return True
    else:
        return False