def primo(n):
    'calcule e retorne se é primo ou não dado um numero n.int-->bool'
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True