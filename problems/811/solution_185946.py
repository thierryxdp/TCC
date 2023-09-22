def colchao(medidas,H,L):
    """Função que calcula e retorna se o colchão que João
    compraria passaria por sua porta, onde "medidas" corresponde
    as medidas do colchão(sendo "A": profundidade, "B":altura e 
    "C":largura), "H" a altura da porta e "L" a largura da porta
    list int int -> bool"""
    medidas= [A,B,C]
    if B>H and C>L:
        return False
    elif B>H and C<L:
        return False
    elif B<H and C>L:
        return False
    elif B<H and C<L:
        return True
    elif B=H and C<L:
        return True
    elif B=H and C>L:
        return False
    elif B>H and C=L:
        return False
    elif B<H and C=L:
        return True