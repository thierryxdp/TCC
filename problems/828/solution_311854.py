def primo(n):
    '''Verifica se um dado número inteiro positivo é primo.
int -> bool'''
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
           return True
 
    else:
        return False