def colchao(medidas,H,L):
    (a,b,c)=medidas #[36,190,209] 187 248 True
    #(a,b)
    #(a,c)
    #(b,c)
    if a*b<H*L:
        return True
    elif a*c<H*L:
        return True
    elif b*c<H*L:
        return True
    else:
        return False