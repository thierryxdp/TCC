def primo(numero):
    for n in range(2,numero):
        if (numero%n)==0:
            return False
    else:
        return True
'''funcao que recebe um numero positivo e retorna 
True caso o numero seja primo, e Falso caso 
nao seja.
int->bool'''