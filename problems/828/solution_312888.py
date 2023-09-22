def primo(valor):
    """Função que diz se o número inteiro dado é primo ou não. Caso seja primo será retornado 'True', caso contrário 'False'."""
    for x in range(2,valor):
        if valor%x==0:
            return False
    else:
        return True