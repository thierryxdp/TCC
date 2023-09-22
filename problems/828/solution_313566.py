def primo(n):
    """Função que dado o numero inteiro positivo indentifique se o número é primo ou não;int->bool"""
    s=1
    for c in range(2,n):
        if n<0:
            return True
        elif n%c==0:
            s=s+1
            return False
        elif s==0:
            return False
        else:
            return False