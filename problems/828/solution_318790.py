def primo(x):
    '''Esta função ao inserir um valor, calcule se um 
    numero é primo ou não
    assinatura int -> int'''
    resltado = [i for i in range(1, x + 1)if x % i == 0]
    if len(resultado) == 2:
        return True
    else:
        return False