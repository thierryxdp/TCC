def primo(numero):'
    '''Funçã
    o que verifica se um número qualquer é primo.int --> bool'''
    i = 0
    
    for elemento in range(2,numero+1)
        if numero % elemento == 0:
            i += 1
    if i == 1:
        return True
    else:
        return False