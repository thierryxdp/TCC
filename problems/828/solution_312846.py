def primo(n):
    '''Função que dado um numero inteiro n, retorna True caso ele seja 
    primo ou False caso nao seja
int -> bool'''
    for x in range(2,n):
        if n%x == 0:
            return False
    return True