def primo(numero):
    """função que dado um numero, retorne se ele é ou não um numero primo;int-->bool"""
    for a in range(2,numero):
        if numero%a==0:
            return False
    return True