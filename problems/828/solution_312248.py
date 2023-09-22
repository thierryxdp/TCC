def primo(n):
    '''Função que dado um n inteiro positivo retorna True se for primo
    e false se não o for. int -> bool'''
    for numero in range(2, n):
        if n % numero == 0:
            x = True
    else:
        x = False
    return x