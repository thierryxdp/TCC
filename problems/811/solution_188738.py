def colchao(medidas,H,L):
    (a,b,c)=medidas
    (a,b)
    (a,c)
    (b,c)
    if (a>=H or a>=L) and (b<H or b<L)and(c<H or c<L):
        return False
    elif (c>=H or c>=L)and (a>=H or a>=L)and(b<H or b<L):
        return False
    elif (b>=H or b>=L)and(a<H or a<L)and(c<H or c<L):
        return False
    else:
        return True