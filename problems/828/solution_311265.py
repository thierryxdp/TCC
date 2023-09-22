def primo(n):
    '''A partir do número inteiro 'n';
retorna se o mesmo é primo ou não;
int => bool'''
    div = 0
    for x in list(range(1,n+1)):
            if n%x == 0:
                div = div+1
    if div == 2:
        return True
    else:
        return False