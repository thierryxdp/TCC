def primo(n):
    """Função que recebe um nmero inteiro positivo n,
    retornando se é numero primo ou não o numero dado
    entrada: int
    retorno: bool"""
    primo= False
    i = 1
    for i in range(1,8):
        if numero% i == 0:
            primo = False
        else:
            primo = True 
    return primo