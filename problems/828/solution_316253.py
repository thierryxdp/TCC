#Essa função avalia se um número é primo ou não.
#int->booleano
def primo(num):
    return num.qtd_divisores() == 2