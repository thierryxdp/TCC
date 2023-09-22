def primo(num):
    '''retorna true se o numero for impar e false se ele
    nao for
    int->bool'''
    x= qtd_divisores(num)
    return x<=2