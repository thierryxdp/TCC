def colchao(medidas,H,L):
    """Função que calcula e retorna se o colchão que João
    compraria passaria por sua porta, onde "medidas" corresponde
    as medidas do colchão(sendo "A": profundidade, "B":altura e 
    "C":largura), "H" a altura da porta e "L" a largura da porta
    list int int -> bool"""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if A>H and C>L:
        return False
    elif A>H and C<L:
        return False
    elif A<H and C>L:
        return True
    elif A<H and C<L:
        return True
    elif C>H and B>L:
        return True
    elif B<H or C>L:
        return True
    elif B>H and C>L:
        return False