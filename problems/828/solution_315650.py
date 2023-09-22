def primo(n):
    'calcule e retorne se é primo ou não dado um numero n.int-->bool'
    multiplos=0
    for i in range(2,n):
        if n%i==0:
            multiplos=multiplos+1
    if multiplos==0:
        return True
    else:
        return False