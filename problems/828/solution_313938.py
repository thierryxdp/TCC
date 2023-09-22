def primo(x):
    '''verifica se o numero inteiro (x) é primo ou nao, retorna o valor 
    booleano True caso seja e False caso nao o seja. int, int-> bool''' 
    y = 0
    for n in range(2,x):
        if(x%n == 0):
            y += 1
    if y == 0:
        return True
    else:
        return False