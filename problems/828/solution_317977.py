def primo(x):
    '''Esta função ao inserir um valor, calcula se um 
    número é primo ou não
    assinatura int -> int'''
    resultado = [i for i in range(1, x + 1) if x % i == 0]
    if len(resultado) == 2:
        return True
    else:
        return False