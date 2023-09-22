def colchao(medidas,H,L):
    """Função que calcule e retorne se o colchão passaria
    da porta da casa do João, assumimos, assim, "medidas" 
    como medidas do colchão, "H" sendo altura da porta e "L",
    por sua vez, largura da porta. "A" - altura do colchão,"B"-
    comprimento do colchão e "C"- largura do colchão
    list int int -> bool"""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if A>H and C<L:
        return False
    elif A>H and C>L:
        return False
    elif A<H and C<L:
        return True
    elif A<H and C>L:
        return True
    elif A<H or C<L:
        return False
    elif A<H or C>L:
        return False