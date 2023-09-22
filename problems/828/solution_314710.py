# A função recebe um número inteiro N positivo e verifica se este número é primo ou não.
# Se o número for primo deverá retornar True senão retornará False
# int-->bool
#
def primo(n):
    i=2
    while i<=round(n/2):
        if n%i==0:
            return False
        i=i+1
    return True