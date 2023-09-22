def primo(numero):
    """função que dado um numero, retorne se ele é ou não um numero primo;int-->bool"""
    for a in range(2,numero):
        if numero%a==1 or numero:
            return False
    return False