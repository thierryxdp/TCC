def primo(n):
    '''Função que verifica se o número 'n' recebido de entrada é primo ou não.
    int->bool'''
    qtd = 1
    for i in range(1,n//2+1):
        if n % i == 0:
            qtd += 1
        elif qtd > 2:
            return False
    if qtd  == 2:
        return True
    else:
        return Fals