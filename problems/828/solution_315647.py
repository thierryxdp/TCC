import math
def primo(n):
    'calcule e retorne se é primo ou não dado um numero n.int-->bool'
    for i in range(1,math.sqrt(n)):
        if n%i==0:
            return True
    else:
        return False