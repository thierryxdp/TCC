def primo(n):
    '''Função retorna se, dado um número, ele é primo ou não
    int -> bool'''
    contador = 0
    for numero in range(2, n):
        if (n%numero == 0):
            contador += 1
            
    if contador == 0:
        return True
    else:
        return False