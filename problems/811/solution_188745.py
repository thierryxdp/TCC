def colchao(medidas,H,L):
    (a,b,c)=medidas #[36,190,209] 187 248 True
    #opcao1=(a,b)
    #opcao2=(a,c)
    #opcao3=(b,c)
    if(a<H and b<L):
        return True
    elif(a<H and c<L):
        return True
    elif(b<H and c<L):
        return True
    
    else:
        return False