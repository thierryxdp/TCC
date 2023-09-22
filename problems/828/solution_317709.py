def primo(numero):
    '''Retorna se um número é primo ou nao, caso seja o valor booleano 'True' será retornado , caso contrário o valor 'False será retornado'''
    '''int->booleano'''
    lista_primos = []
    for valor in range(numero):
        if valor != 0 and valor!=1:
            if numero % valor == 0:
                return False
    return True