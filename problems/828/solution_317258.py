def primo(n):
    '''Função que retorna se o número é primo ou não, int -> bool'''
    x = 0 
    n = 0
    for primos in range(1, n + 1):
        if(n%primos == 0):
            x = x + 1
        if (x == 2):
            return True 
        else:
            return False