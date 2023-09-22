def primo(n):
	'''funcao que descobre se um numero e primo ou nao;
    int -> bool'''
    div = 0
    for x in range (1,n+1):
        z = n%x
        if z == 0:
            div = div + 1
    if div > 2:
        return False
    else:
        return True