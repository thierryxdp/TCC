def primo(n):
    """Função que recebe um nmero inteiro positivo n,
    retornando se é numero primo ou não o numero dado
    entrada: int
    retorno: bool"""
    primo= True
    i = 1
    for i in range(1,8):
        if n > 3:
            if n%% i == 0:
                return False
    return primo