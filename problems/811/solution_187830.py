def colchao(medidas,h,l):
    medidas = [a,b,c]
    if a<=l and c<=h:
        return True 
    elif b<=l and c<=h:
        return True
    elif c<=l and b<=h:
        return True
    elif a<=l and b<=h :
        return True 
    elif c<=l and a<=h:
        return True 
    elif b<=l and a<=h:
        return True 
    else:
        return False