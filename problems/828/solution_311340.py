def primo(n):
    """Função indica se o número dado é primo ou não;
       int->bool
       Parâmetro:
       n: número qualquer
    """
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True