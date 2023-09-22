def primo(numero):
    '''Função que dado um número inteiro positivo, verifique se este
    número é primo ou não
    int -> bool'''
    
    divisores = 0
    
    for n in list(range(2,numero)):
        if (numero%n) == 0:
            divisores = divisores + 1
    if divisores == 0:
        return True
    else:
        return False