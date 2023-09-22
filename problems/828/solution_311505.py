def primo(n):
    '''uma função que dado um número inteiro retorna se o número é primo ou não.
    int -> bool'''
    contador = 0
    for primo in range(n):
        if n%(primo+1)==0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False