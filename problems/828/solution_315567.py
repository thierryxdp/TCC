def primo(x):
    'verifica se o numero é primo ou nao, retorna um booleano'
    'entrada: int'
    'saida: bool'
    num = 0
    for n in range (1,n+1):
        if x%n == 0:
            num+=1
    if num == 2:
        return True
    else:
        return False