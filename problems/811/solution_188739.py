def colchao(medidas,H,L):
    (a,b,c)=medidas 36,190,209
    (a,b)
    (a,c)
    (b,c)
    if (a>=H or a>=L) and ((b<H or b<L)or(c<H or c<L)):
        return False
    elif (c>=H or c>=L)and((a>=H or a>=L)or(b<H or b<L)):
        return False
    elif (b>=H or b>=L)and((a<H or a<L)or(c<H or c<L)):
        return False
    else:
        return True