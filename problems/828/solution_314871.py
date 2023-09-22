def primo(num):
    """dado um numero inteiro positivo, verifica
    se esse é primo ou nao.
    int->bool"""
    poss=list(range(2,int(num/2)))
    for chance in poss:
        if num%chance==0:
            return False
        else:
            return True