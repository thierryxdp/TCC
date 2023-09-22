def primo(n):
    ''' Função que responde se o numero é primo ou não
    int-> bool'''
    
    primo=1
    if n < 0:
        return "Error"
    for i in range(1, int(n//2+1)):
        if n % i == 0:
            primo=primo+1

    if primo > 2:
        return False
    else:
        return True