def primo(valor):
    """Dado um valor, a função dirá se é
    primo ou não. int->bool"""
    tot=0
    for c in range(1,valor+1):
        if valor%c==0:
            tot+=1
    if tot==2:
        return True
    else:
        return False