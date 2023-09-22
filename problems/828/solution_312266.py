def primo(n):
    '''Função que dado um número "n" de entrada, retorna se esse número é
    primo ou não.'''
    #Utilizando a função da questão anterior.
    divisores = 0
    for i in range(1, n+1):
        if (n % i) == 0:
            divisores += 1
    #Se "divisores" é igual 2, o número é primo, ccaso contrário ele não
    #é primo.
    if divisores == 2:
        return True
    else:
        return False