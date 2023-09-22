#Funcao que dado um numero n sera retornado o valor booleano True se n for
#um numero primo e False caso nao seja
#Entrada int > saida bool

def primo(n):
    i = 1
    divisores = 0
    while i<=n:
        if n%i == 0:
            divisores = divisores + 1
        i = i + 1
    return divisores == 2