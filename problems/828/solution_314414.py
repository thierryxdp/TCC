def primo(n):
    '''Program aque lê um número inteiro n e retorna se ele é primo ou não
    int -> bool'''
    m = 0
    if n != 0 and n !=1:
        if n > 3:
            for i in range(2,n):
                if (n % i == 0):
                    m = m+1
                return False
        return True
    return False