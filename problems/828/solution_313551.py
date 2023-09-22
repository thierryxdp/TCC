def primo(n):
    """Função que dado o numero inteiro positivo indentifique se o número é primo ou não;int->bool"""
    for c in range(1,n+1):
        if n<0:
            return False
        elif n%c==0:
            return True
        else:
            return False