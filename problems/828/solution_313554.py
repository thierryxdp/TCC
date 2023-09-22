def primo(n):
    """Função que dado o numero inteiro positivo indentifique se o número é primo ou não;int->bool"""
    s=0
    for c in range(2,n):
        if n<0:
            return False
        elif n%c==0:
            s=s+1
            return True
        elif s==0:
            return True
        else:
            return False