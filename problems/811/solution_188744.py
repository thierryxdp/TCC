def colchao(medidas,H,L):
    (a,b,c)=medidas #[36,190,209] 187 248 True
    #(a,b)
    #(a,c)
    #(b,c)
    if (a>H or b>L)and(a>H or c>L)and(b>H or c>L)
        return False
    
    else:
        return True