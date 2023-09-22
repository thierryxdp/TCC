def primo(n):
    '''retorna True caso o numero (n) fornecido for primo e False caso contrario
    int -> bool'''
    for num in range(2,n):
        if n%num == 0:
            return False
    else: 
        return True