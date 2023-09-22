#A função recebe como entrada um número inteiro positivo e retorna se ele é ou não primo
#assinatura: int-->bool
def primo(n):
    if n==1:
        return False
    x=0
    for y in range(2, n):
        if (n%y==0):
            x=+1
        if x==0:
            return True
        else:
            return False