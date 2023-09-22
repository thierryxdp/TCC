# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Substitui algum termo da string e retorna'''
    comprimento = len(s)
    if (0<=i<=comprimento):
        x = s[i]
        return x
    else:
        return False