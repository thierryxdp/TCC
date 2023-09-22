def primo(n):
    '''Função que dado um numero inteiro positivo, retorna verdadeiro se ele for primo e falso se não for:
    int -> bool'''
    multiplos = 0
    for numero in range(2,n):
        if n%numero == 0:
            return False
        else:
            return True