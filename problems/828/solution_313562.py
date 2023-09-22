def primo(n):
    """Função que dado o numero inteiro positivo indentifique se o número é primo ou não;int->bool"""
    s=0
    for c in range(2,n+1):
        if n<0:
            return False
        elif n%c==0:
            s=s+1
            return False
        elif s==0:
            return False
        else:
            return False
    return True