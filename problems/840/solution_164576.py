def bolos(A,B,C):
    """calcula a quantidade A de xicars de farinha divido por dois, a quantidade B de ovos divido por tres, a quantidade C de colheres de leite divido por cinco, e retorna o menor valor entre as divisoes"""
    An=A/2
    Bn=B/3
    Cn=C/5
    return min(An,Bn,Cn)