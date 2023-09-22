def primo(num):
    """dado um numero inteiro positivo, verifica
    se esse é primo ou nao.
    int->bool"""
    poss=list(range(2,num))
    controle=[]
    for chance in poss:
        if num%chance==0:
            list.append(controle,1)
    if len(controle)>0:
        return False
    else:
        return True