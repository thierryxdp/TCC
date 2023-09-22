def colchao(medidas,H,L):
    """Recebe as medidas do colchao e da porta e define se o colchao
    	passaria ou nao pela porta. 
        entradas float, float, float, int, int --> saida bool"""
    m1=medidas[0]
    m2=medidas[1]
    m3=medidas[2]
    if (m1<H and m2<L) or (m2<H and m1<L) or (m1<H and m3<L)
    or (m3<H and m3<L) or (m3<H and m2<L) or (m2<H and m3<L)
    or (m1<H and (m3 and m2)<L) or (m2<H and (m1 and m3)<L)
    or (m3<H and (m1 and m2)<L) or ((m1 and m2)<H and (m3<L))
    or ((m1 and m3)<H and (m2<L)) or 
    ((m2 and m3)<H and (m1<L)):
        return True
    else:
        return False