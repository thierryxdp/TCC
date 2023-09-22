def primo (n):
    '''Função verifica se o número inteiro fornecido é primo ou não. 
    int -> boolean'''
    for i in range (2,n):
        if n%i == 0:
            return False
    return True