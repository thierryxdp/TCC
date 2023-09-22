def colchao(medidas,H,L):
    """Recebe as medidas do colchao e da porta e define 
       se o colchao passaria ou nao pela porta. 
       entradas float, float, float, int, int --> saida bool"""
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if (A<H and B<L) or (B<H and A<L) or (A<H and C<L) or (C<H and C<L) or (C<H and B<L) or (B<H and C<L)
    or (A<H and (C and B)<L) or (B<H and (A and C)<L) or (C<H and (A and B)<L) or ((A and B)<H and (C<L))
    or ((A and C)<H and (B<L)) or ((B and C)<H and (A<L)):
        return True
    else:
        return False