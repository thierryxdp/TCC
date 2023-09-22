def primo(n):
    """Função indica se o número dado é primo ou não;
       int->bool
       Parâmetro:
       n: número qualquer
    """
    for i in range(2,n):
        if not n%i==0:
            return True
    else:
        return False